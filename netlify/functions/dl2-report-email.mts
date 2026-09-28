import type { FormSubmittedEvent } from '@netlify/functions';
import { getStore } from '@netlify/blobs';
import { deliverReport } from './_shared/delivery.mts';
import { gmailSender } from './_shared/mail.mts';

// Native event-only handler: Netlify authenticates its event signature before
// invoking this function. No public upload or email-sending HTTP route is exposed.
export default {
  async formSubmitted(event: FormSubmittedEvent) {
    if (Netlify.context?.deploy.context !== 'production' || Netlify.env.get('DL2_PDF_EMAIL_ENABLED') !== 'true') return;
    if (!/^DL2-(PRE|POST)-/.test(event.data['record-id'] || '')) return;
    const password = Netlify.env.get('DL2_GMAIL_APP_PASSWORD');
    const sender = password ? gmailSender(password) : null;
    const store = getStore({ name: 'dl2-report-delivery', consistency: 'strong' });
    try {
      const state = await deliverReport(event.data, store, sender);
      // Log status only: never student identity, answers, credentials or PDF bytes.
      console.log('DL2 PDF email:', state);
    } catch {
      console.error('DL2 PDF email: validation or storage failure; original record remains in Forms');
      throw Error('DL2 attachment processing failed');
    }
  }
};
