import { test } from 'node:test';
import assert from 'node:assert/strict';
import Items from '../../courses/digital-literacy-2/os/items.js';
import Grade from '../../courses/digital-literacy-2/os/grade.js';
import * as PDFLib from '../../courses/digital-literacy-2/os/vendor/pdf-lib.min.js';
import { reportFromFields, buildAttachment } from '../../netlify/functions/_shared/report.mts';
import { deliverReport } from '../../netlify/functions/_shared/delivery.mts';
import { gmailSender } from '../../netlify/functions/_shared/mail.mts';

function fields(form = 'pre') {
  const answers = Items[form].map(i => i.answer);
  if (form === 'post') answers[0] = Items.post[0].answer === 'A' ? 'B' : 'A';
  const r = Grade.grade(Items[form], answers);
  return { 'form-name': 'dl2-' + form + 'test', 'bot-field': '', 'record-id': 'DL2-' + form.toUpperCase() + '-20260928-1057-ST-1234abcd', student: 'SYNTHETIC Attachment Test', form: form + ' ' + Items.version, started: '2026-09-28T14:30:00.000Z', submitted: '2026-09-28T14:57:00.000Z', score: r.correct + '/20', domains: r.byDomain.map(d => d.id + ':' + d.correct + '/' + d.total).join(' '), answers: answers.join(',') };
}
function memoryStore() {
  const map = new Map(); let revision = 0;
  return {
    async getWithMetadata(key, _options) { return map.get(key) || null; },
    async setJSON(key, value, options?) {
      const old = map.get(key);
      if (options?.onlyIfNew && old || options?.onlyIfMatch && options.onlyIfMatch !== old?.etag) return { modified: false };
      map.set(key, { data: value, etag: String(++revision) }); return { modified: true };
    },
    states: () => [...map.values()].map(v => v.data.state)
  };
}
for (const form of ['pre', 'post']) test(form + ' uses canonical score and creates an openable two-page branded PDF', async () => {
  const { report } = reportFromFields(fields(form));
  assert.equal(report.result.correct, form === 'pre' ? 20 : 19);
  assert.equal(report.result.rows.length, 20); assert.equal(report.result.byDomain.length, 7);
  const a = await buildAttachment(report);
  const pdf = await ((PDFLib as any).default || PDFLib).PDFDocument.load(a.bytes);
  assert.equal(pdf.getPageCount(), 2); assert.equal(pdf.getTitle(), report.recordId);
  assert.equal(pdf.getAuthor(), 'West Virginia Veterans Upward Bound');
});
test('rejects tampered scores, domains, answers, version, IDs, dates and oversized input', () => {
  for (const patch of [{ score: '0/20' }, { domains: '' }, { answers: 'A' }, { answers: Array(20).fill('X').join(',') }, { form: 'pre unknown' }, { 'record-id': '../secret' }, { submitted: 'yesterday' }, { started: '2026-09-29T14:30:00.000Z' }, { student: 'x'.repeat(121) }, { 'bot-field': 'bot' }, { junk: 'x'.repeat(9000) }]) assert.throws(() => reportFromFields({ ...fields(), ...patch }));
});
test('fixed Gmail account and genuine PDF attachment; ignores attacker recipient/file fields', async () => {
  let options, message, verified = false, closed = false;
  const sender = gmailSender('abcd efgh ijkl mnop', (config => {
    options = config;
    return { verify: async () => { verified = true; }, close: () => { closed = true; }, sendMail: async mail => {
      assert.ok(verified); message = mail;
      return { accepted: ['britt.legg76@gmail.com'], rejected: [], messageId: 'synthetic-receipt' };
    } };
  }) as any);
  const store = memoryStore();
  assert.equal(await deliverReport({ ...fields(), to: 'attacker@example.com', pdf: 'malicious' }, store, sender), 'accepted');
  assert.equal(options.host, 'smtp.gmail.com'); assert.equal(options.port, 465); assert.equal(options.secure, true);
  assert.equal(options.auth.user, 'britt.legg76@gmail.com'); assert.equal(options.auth.pass, 'abcdefghijklmnop');
  assert.equal(message.to, 'britt.legg76@gmail.com'); assert.equal(message.from.address, message.to);
  assert.equal(message.attachments[0].contentType, 'application/pdf'); assert.equal(message.attachments[0].contentDisposition, 'attachment');
  const pdf = await ((PDFLib as any).default || PDFLib).PDFDocument.load(message.attachments[0].content);
  assert.equal(pdf.getPageCount(), 2); assert.ok(closed);
});
test('simultaneous and later duplicate events send once', async () => {
  let sends = 0; const store = memoryStore();
  const send = async () => { sends++; return 'receipt'; };
  await Promise.all([deliverReport(fields(), store, send), deliverReport(fields(), store, send)]);
  assert.equal(await deliverReport(fields(), store, send), 'accepted'); assert.equal(sends, 1);
});
test('missing configuration stays recorded without sending, and later configuration can send', async () => {
  const store = memoryStore();
  assert.equal(await deliverReport(fields(), store, null), 'not-configured');
  assert.equal(await deliverReport(fields(), store, async () => 'receipt'), 'accepted');
});
test('uncertain provider outcome is not blindly resent', async () => {
  const store = memoryStore(); let sends = 0;
  const send = async () => { sends++; throw Error('timeout'); };
  assert.equal(await deliverReport(fields(), store, send), 'needs-review');
  assert.equal(await deliverReport(fields(), store, send), 'needs-review'); assert.equal(sends, 1);
});
test('reusing an ID with changed answers or identity is rejected', async () => {
  const store = memoryStore(); await deliverReport(fields(), store, null);
  await assert.rejects(deliverReport({ ...fields(), student: 'Another Student' }, store, async () => 'receipt'), /Record ID conflict/);
});
test('SMTP verification failure never sends or records accepted', async () => {
  const store = memoryStore(); let sends = 0;
  const send = gmailSender('abcdefghijklmnop', (() => ({ verify: async () => { throw Error('bad auth'); }, close: () => {}, sendMail: async () => { sends++; } })) as any);
  assert.equal(await deliverReport(fields(), store, send), 'needs-review');
  assert.deepEqual(store.states(), ['needs-review']); assert.equal(sends, 0);
});
test('the native event handler stays disabled outside production or without the activation flag', async () => {
  const handler = (await import('../../netlify/functions/dl2-report-email.mts')).default;
  const previous = globalThis.Netlify;
  try {
    for (const context of ['dev', 'deploy-preview', 'production']) {
      globalThis.Netlify = { context: { deploy: { context } }, env: { get: () => context === 'production' ? undefined : 'true' } } as any;
      await handler.formSubmitted({ data: fields() });
    }
  } finally { globalThis.Netlify = previous; }
});
