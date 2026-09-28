import { createHash } from 'node:crypto';
import { readFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import Items from '../../../courses/digital-literacy-2/os/items.js';
import Grade from '../../../courses/digital-literacy-2/os/grade.js';
import Paper from '../../../courses/digital-literacy-2/os/paper.js';
import createPdf from '../../../courses/digital-literacy-2/os/pdf.js';
import * as PDFLib from '../../../courses/digital-literacy-2/os/vendor/pdf-lib.min.js';
import * as fontkit from '../../../courses/digital-literacy-2/os/vendor/fontkit.umd.min.js';

// Only answers are trusted as input. Scores, categories, answer text and PDF bytes
// are derived from the same canonical item bank and renderer used in the browser.
export function reportFromFields(data: Record<string, unknown>) {
  if (!data || typeof data !== 'object' || JSON.stringify(data).length > 8192) throw Error('Invalid submission size');
  const field = (key: string, max: number) => {
    const value = data[key];
    if (typeof value !== 'string' || value.length > max || /[\x00-\x1f\x7f]/.test(value)) throw Error('Invalid ' + key);
    return value;
  };
  if (data['bot-field']) throw Error('Honeypot');
  const formVersion = field('form', 40);
  const form = formVersion.split(' ')[0] as 'pre' | 'post';
  if (!['pre', 'post'].includes(form) || formVersion !== form + ' ' + Items.version) throw Error('Unsupported assessment version');
  if (data['form-name'] && data['form-name'] !== 'dl2-' + form + 'test') throw Error('Form mismatch');
  const name = field('student', 120).trim();
  if (name.length < 2) throw Error('Invalid name');
  const recordId = field('record-id', 70);
  if (!new RegExp('^DL2-' + form.toUpperCase() + '-\\d{8}-\\d{4}-[A-Z]{1,2}-[a-f0-9]{8}$').test(recordId)) throw Error('Invalid record ID');
  const dates = ['started', 'submitted'].map(key => {
    const str = field(key, 24), date = new Date(str);
    if (!Number.isFinite(+date) || date.toISOString() !== str) throw Error('Invalid timestamp');
    return date;
  });
  const [started, submitted] = dates;
  if (+submitted < +started || +submitted - +started > 7 * 86400000) throw Error('Invalid duration');
  const answers = field('answers', 39).split(',');
  if (answers.length !== 20 || answers.some(a => !/^[ABCD-]$/.test(a))) throw Error('Invalid answers');
  const items = Items[form];
  const result = Grade.grade(items, answers.map(a => a === '-' ? null : a));
  const score = result.correct + '/' + result.total;
  const domains = result.byDomain.map((d: { id: string; correct: number; total: number }) => d.id + ':' + d.correct + '/' + d.total).join(' ');
  if (data.score !== score || data.domains !== domains) throw Error('Submitted score differs from canonical grading');
  const report = { form, label: form === 'pre' ? 'Pre-Test' : 'Post-Test', items, result, name, started, submitted, recordId };
  const digest = createHash('sha256').update(JSON.stringify({ name, formVersion, started, submitted, recordId, answers })).digest('hex');
  return { report, digest };
}

export async function buildAttachment(report: ReturnType<typeof reportFromFields>['report']) {
  const allowed = new Set(['fonts/playfair-display-latin-800-normal.woff', 'fonts/source-sans-3-latin-400-normal.woff', 'fonts/source-sans-3-latin-700-normal.woff', 'img/vub-seal-360.png']);
  const pdf = createPdf({ PDFLib: (PDFLib as any).default || PDFLib, fontkit: (fontkit as any).default || fontkit, DL2Paper: Paper, DL2Items: Items }, async (asset: string) => {
    if (!allowed.has(asset)) throw Error('Unknown report asset');
    return readFile(resolve('courses/digital-literacy-2/os', asset));
  });
  const bytes = Buffer.from(await pdf.build(report));
  if (bytes.length > 1000000 || bytes.subarray(0, 5).toString() !== '%PDF-') throw Error('Invalid PDF');
  return { filename: report.recordId + '.pdf', bytes };
}
