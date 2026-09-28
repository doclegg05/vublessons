# Graded PDF attachment delivery

Status: implemented and locally tested; **not enabled or verified in production**.
The existing production Forms notifications and student PDF/USB backup continue working.
Britt confirmed receipt of both field-only test emails on September 28, 2026.

## What the implementation does

`netlify/functions/dl2-report-email.mts` listens only for Netlify's authenticated
`formSubmitted` event for verified submissions. It has no public HTTP send endpoint.
Only production events run, and only when `DL2_PDF_EMAIL_ENABLED=true`.

The server validates the supported assessment version, name, record ID, timestamps,
20 answer letters, and payload size. It recalculates every score/category/answer using
`os/items.js` and `os/grade.js`, rejecting mismatched client totals. It then uses the
same `os/pdf.js` renderer, bundled fonts and seal as the student's report. No uploaded
PDF, URL, client-supplied recipient or answer text is used. The only destination is
Britt's already verified instructor address. Browser requests still go to Netlify Forms;
the existing offline outbox and independent USB-download instructions stay intact.

The private `dl2-report-delivery` Blobs store holds a hashed record key, data fingerprint,
state and provider receipt, not the learner's name, answers or PDF. Atomic claims prevent
concurrent sends. Repeated accepted records are skipped. Changed data with an existing
record ID is rejected. If a provider timeout or interrupted worker makes delivery
uncertain, the state remains `needs-review` (or `sending`) and automatic resend is
suppressed. An instructor/operator must reconcile against the provider before retrying.
The original data remains available in Netlify Forms, including submissions needing
manual spam review. Netlify's acceptance does not mean an email reached an inbox.

## Missing setup

Britt selected his instructor Gmail account with a dedicated Google app password.
No app password has been supplied. No account, subscription or credential was created.

1. Sign in to `britt.legg76@gmail.com` at https://myaccount.google.com/apppasswords .
   Create an app password named **VUB graded PDF reports**. Google requires 2-Step
   Verification. If unavailable due to account policy, security-key-only verification
   or Advanced Protection, report that constraint; do not weaken those settings.
2. In https://app.netlify.com/projects/vubcourse/configuration/env choose **Add a
   variable > Add a single variable**. Key: `DL2_GMAIL_APP_PASSWORD`. Paste the
   generated 16-character app password into Netlify only. Mark **Contains secret
   values** and use **Production** only. Prefer **Functions** scope when available.
   The current account plan locks secret scope to Builds, Functions and Runtime;
   Functions-only requires an upgrade. Explicit instructor acceptance of those
   broader production scopes is required before saving on this plan. Do not
   upgrade or broaden the scope automatically.
   Never paste it in chat, browser source, the repository or public build files.
3. Keep `DL2_PDF_EMAIL_ENABLED` unset/false until the prepared deployment is ready
   for the authorized synthetic test. The agent can set this non-secret activation
   flag and redeploy after Britt confirms secure entry of the password.

Both SMTP login and recipient are fixed to `britt.legg76@gmail.com`. The server connects
to `smtp.gmail.com:465` with verified TLS, authenticates, and sends a Buffer attachment
with content type `application/pdf` and disposition `attachment`. It cannot read arbitrary
files or URL attachments. SMTP debug logging is disabled. It uses neither an ordinary
Google password nor another project's credentials. Existing Netlify notification hooks
stay enabled as a separate fallback.

## Activation / acceptance

1. Securely enter the dedicated Gmail app password as described above.
2. Run `npm run test:report-email`, the normal quality gate, and package the function.
3. Deploy via the normal reviewed Git/Netlify route and enable the production gate.
4. Submit one clearly labeled synthetic assessment using the live student UI. Verify
   the stored Forms record and event-function state. Check Spam if necessary.
5. Confirm a real PDF **attachment** arrives in Britt's inbox, opens, and matches the
   name, test/version, score, seven domains, twenty graded answers and record ID.
6. Confirm repeat delivery of the same event creates no additional attachment email.
7. Record the provider receipt and Britt's inbox confirmation. Do not claim activation
   complete merely because a local mocked mail request or Netlify HTTP POST succeeded.

The student screen continues to state only that Netlify accepted the result. It does not
promise attachment receipt. The instructor guide describes the pending attachment setup and operational handling
of missing mail. Change its status only after the live attachment test passes.

## Recovery

Do not delete the delivery ledger or keep clicking student Submit to force another email.
Check the provider for the receipt/message first. For a definite provider rejection,
use the original saved Netlify record to prepare a deliberate operator replay, preserving
its record ID; clear only the matching failed claim after confirming no email was sent.
No public replay endpoint is shipped. For ambiguous delivery, use the existing USB PDF
or Forms record while investigating. This deliberately favors avoiding duplicate mail
over silently assuming a timeout meant no send.

## Evidence

- Ten local server tests cover canonical grading/PDFs, malicious/mismatched fields,
  fixed recipient, real PDF attachment, concurrent/later duplicates, missing settings,
  ambiguous provider failures, record conflicts and the production activation gate.
- Twenty-nine existing assessment/PDF browser tests passed after renderer reuse.
- Both local synthetic PDFs parse as two pages; text and branded visual layout checked.
- No real attachment email has yet been sent; credential/setup is still required.

Sources: https://docs.netlify.com/build/functions/trigger-on-events/
https://docs.netlify.com/manage/forms/notifications/
https://docs.netlify.com/build/data-and-storage/netlify-blobs/
https://support.google.com/accounts/answer/185833
https://nodemailer.com/smtp
https://nodemailer.com/message/attachments
