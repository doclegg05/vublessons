import nodemailer from 'nodemailer';
import type { Sender } from './delivery.mts';

// Both account and destination are fixed. Client fields cannot turn this into a relay.
export function gmailSender(appPassword: string, createTransport: typeof nodemailer.createTransport = nodemailer.createTransport): Sender {
  const password = appPassword.replace(/\s/g, '');
  if (!/^[a-zA-Z0-9]{16}$/.test(password)) throw Error('Invalid Gmail app-password configuration');
  return async mail => {
    const account = 'britt.legg76@gmail.com';
    const transport = createTransport({ host: 'smtp.gmail.com', port: 465, secure: true,
      auth: { user: account, pass: password },
      tls: { minVersion: 'TLSv1.2', rejectUnauthorized: true },
      connectionTimeout: 10000, greetingTimeout: 10000, socketTimeout: 15000,
      logger: false, debug: false, disableFileAccess: true, disableUrlAccess: true });
    try {
      // Check authentication before sending. The delivery ledger conservatively
      // holds all SMTP failures for review rather than assuming a timeout was safe.
      await transport.verify();
      const info = await transport.sendMail({
        from: { name: 'VUB Assessment Reports', address: account }, to: account,
        subject: mail.subject, text: mail.text,
        messageId: '<' + mail.key + '@vublessons.com>',
        attachments: [{ filename: mail.attachment.filename, content: mail.attachment.bytes,
          contentType: 'application/pdf', contentDisposition: 'attachment' }],
        disableFileAccess: true, disableUrlAccess: true
      });
      if (!info.accepted?.includes(account) || info.rejected?.length) throw Error('Gmail did not accept the instructor destination');
      return info.messageId;
    } finally { transport.close(); }
  };
}
