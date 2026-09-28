// Week 1 class files: the Community Supper flyer (Mission 1C) and the headset sound test (Mission 1B), and the links
// to them from the run sheet and the missions worksheet.
const { test, expect } = require('@playwright/test');
const fs = require('fs');
const path = require('path');
const zlib = require('zlib');
const DIR = path.join(__dirname, '../../courses/digital-literacy-2/weeks/week-01');
const DOCX = path.join(DIR, 'files/Community Supper Flyer.docx');
const URL = '/courses/digital-literacy-2/weeks/week-01/';

// Minimal ZIP reader: walks the central directory; entries are stored or deflated.
function unzip(buf) {
  const eocd = buf.lastIndexOf(Buffer.from([0x50, 0x4b, 0x05, 0x06]));
  const count = buf.readUInt16LE(eocd + 10), out = {};
  let off = buf.readUInt32LE(eocd + 16);
  for (let i = 0; i < count; i++) {
    const method = buf.readUInt16LE(off + 10), csize = buf.readUInt32LE(off + 20);
    const nlen = buf.readUInt16LE(off + 28), xlen = buf.readUInt16LE(off + 30), clen = buf.readUInt16LE(off + 32);
    const local = buf.readUInt32LE(off + 42), name = buf.toString('utf8', off + 46, off + 46 + nlen);
    const start = local + 30 + buf.readUInt16LE(local + 26) + buf.readUInt16LE(local + 28);
    const raw = buf.subarray(start, start + csize);
    out[name] = (method === 0 ? raw : zlib.inflateRawSync(raw)).toString('utf8');
    off += 46 + nlen + xlen + clen;
  }
  return out;
}
const attr = (xml, name) => { const m = xml.match(new RegExp(`w:${name}="(\\d+)"`)); return m ? Number(m[1]) : null; };
const paragraphs = xml => [...xml.matchAll(/<w:p[ >][\s\S]*?<\/w:p>/g)].map(m => {
  const p = m[0], sp = (p.match(/<w:spacing [^>]*\/>/) || [''])[0];
  return { text: [...p.matchAll(/<w:t(?: [^>]*)?>([^<]*)<\/w:t>/g)].map(t => t[1]).join(''), rule: (sp.match(/w:lineRule="(\w+)"/) || [])[1],
    line: attr(sp, 'line') / 20, before: attr(sp, 'before'), after: attr(sp, 'after') / 20, breaks: /<w:br\b/.test(p) };
});
// Lay the single-line paragraphs out top to bottom; return the indexes of paragraphs that start a new page.
function pageStarts(paras, room) {
  const starts = []; let y = 0;
  paras.forEach((p, i) => { if (y > 0 && y + p.line > room) { starts.push(i); y = 0; } y += p.line + p.after; });
  return starts;
}

test('the flyer is a real Word document with the Mission 1C text', () => {
  const parts = unzip(fs.readFileSync(DOCX));
  for (const part of ['[Content_Types].xml', '_rels/.rels', 'word/document.xml']) expect(Object.keys(parts), part).toContain(part);
  expect(parts['[Content_Types].xml']).toContain('application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml');
  expect(parts['_rels/.rels']).toContain('Target="word/document.xml"');
  const text = paragraphs(parts['word/document.xml']).map(p => p.text);
  expect(text[0]).toBe('Community Supper');
  expect(text[1]).toBe('Thursday, October 8 · 5:30 PM · Grace Fellowship Hall');
  expect(text).toContain('Free supper for veterans and families');
  expect(text[text.length - 1]).toBe('Questions? Call (555) 010-0148');
});

test('Normal margins push exactly the last line to page 2; Narrow margins fit one page', () => {
  const xml = unzip(fs.readFileSync(DOCX))['word/document.xml'];
  const sect = xml.match(/<w:sectPr[\s\S]*<\/w:sectPr>/)[0];
  const size = sect.match(/<w:pgSz [^>]*\/>/)[0], mar = sect.match(/<w:pgMar [^>]*\/>/)[0];
  expect([attr(size, 'w'), attr(size, 'h')]).toEqual([12240, 15840]);
  expect(['top', 'bottom', 'left', 'right', 'header', 'footer'].map(k => attr(mar, k))).toEqual([1440, 1440, 1440, 1440, 720, 720]);
  const paras = paragraphs(xml);
  for (const p of paras) {
    expect(p, JSON.stringify(p)).toMatchObject({ rule: 'exact', before: 0, breaks: false });
    expect(p.text.length, p.text).toBeGreaterThan(0);
    expect(p.text.length, `${p.text} stays on one line`).toBeLessThanOrEqual(56);
  }
  const heightPt = (15840 - 2 * 1440) / 20, narrowPt = (15840 - 2 * 720) / 20; // 648pt and 720pt of body
  expect(pageStarts(paras, heightPt)).toEqual([paras.length - 1]);
  expect(pageStarts(paras, narrowPt)).toEqual([]);
  const total = paras.reduce((n, p, i) => n + p.line + (i < paras.length - 1 ? p.after : 0), 0);
  expect(total).toBeGreaterThan(heightPt + 10);
  expect(total).toBeLessThan(narrowPt - 40);
});

test('the site serves both class files', async ({ request }) => {
  const docx = await request.get(URL + 'files/Community%20Supper%20Flyer.docx');
  expect(docx.status()).toBe(200);
  expect((await docx.body()).subarray(0, 2).toString()).toBe('PK');
  expect((await request.get(URL + 'files/sound-test.html')).status()).toBe(200);
});

test('the run sheet and the missions link the class files; printed wording stays', async ({ page }) => {
  await page.goto(URL + 'run-sheet.html');
  const before = page.locator('.checklist');
  await expect(before.locator('a[download][href$="files/Community Supper Flyer.docx"]')).toHaveText('Community Supper Flyer.docx');
  await expect(before.locator('a[href$="files/sound-test.html"]')).toHaveCount(1);
  await page.goto(URL + 'worksheet.html');
  const b5 = page.locator('#m1B .mission-steps > li').nth(4), c1 = page.locator('#m1C .mission-steps > li').nth(0);
  await expect(b5).toContainText('Play the test sound Britt shares.');
  await expect(b5.locator('.where a[href$="files/sound-test.html"]')).toHaveCount(1);
  await expect(c1).toContainText('Open Community Supper Flyer.docx from the class folder.');
  await expect(c1.locator('.where a[download][href$="files/Community Supper Flyer.docx"]')).toHaveCount(1);
});
