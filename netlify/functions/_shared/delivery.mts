import { createHash } from 'node:crypto';
import { reportFromFields, buildAttachment } from './report.mts';

type Store = {
  getWithMetadata: (key: string, options: { type: 'json' }) => Promise<any>;
  setJSON: (key: string, value: unknown, options?: { onlyIfNew: true; onlyIfMatch?: never } | { onlyIfMatch: string; onlyIfNew?: never }) => Promise<{ modified: boolean }>;
};
type Mail = { subject: string; text: string; attachment: { filename: string; bytes: Buffer }; key: string };
export type Sender = (mail: Mail) => Promise<string>;

// Receipts contain no student names/answers/PDFs. The original verified data stays
// in Netlify Forms. Atomic claims prevent simultaneous event/retry sends.
export async function deliverReport(data: Record<string, unknown>, store: Store, sender: Sender | null, now = Date.now()) {
  const { report, digest } = reportFromFields(data);
  const key = createHash('sha256').update(report.recordId).digest('hex');
  const previous = await store.getWithMetadata(key, { type: 'json' });
  const old = previous?.data;
  if (old && old.digest !== digest) throw Error('Record ID conflict');
  if (old?.state === 'accepted') return 'accepted';
  // Do not automatically repeat a send whose outcome is unknown. An operator must
  // reconcile it with the provider first, including if a worker stopped mid-send.
  if (old?.state === 'sending' || old?.state === 'needs-review') return 'needs-review';
  const base = { digest, updatedAt: new Date(now).toISOString() };
  const condition = previous ? { onlyIfMatch: previous.etag } : { onlyIfNew: true as const };
  if (!sender) {
    await store.setJSON(key, { ...base, state: 'not-configured' }, condition);
    return 'not-configured';
  }
  // Build before claiming: rendering failures must never imply that an email went out.
  const attachment = await buildAttachment(report);
  const claim = await store.setJSON(key, { ...base, state: 'sending' }, condition);
  if (!claim.modified) return 'pending';
  try {
    const providerId = await sender({
      subject: 'VUB ' + report.label + ' graded results — ' + report.recordId,
      text: [report.label + ' graded results for ' + report.name,
        'Score: ' + report.result.correct + '/20', 'Record: ' + report.recordId,
        'The attached PDF includes all graded answers and domain totals.',
        'Keep the student flash-drive copy as an independent backup.'].join('\n'),
      attachment, key: 'dl2-' + key
    });
    await store.setJSON(key, { ...base, state: 'accepted', providerId });
    return 'accepted';
  } catch {
    // A network timeout can occur after the provider accepted an email. Preserve
    // this ambiguity; never blindly auto-resend and create another attachment email.
    await store.setJSON(key, { ...base, state: 'needs-review' });
    return 'needs-review';
  }
}
