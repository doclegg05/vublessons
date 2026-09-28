// DL2 Mission Control ships its own fonts and PDF libraries (no CDN).
const { test, expect } = require('@playwright/test');
const path = require('path');
const fs = require('fs');
const OS = path.join(__dirname, '../../courses/digital-literacy-2/os');

test('fonts, vendor libraries and the seal are served', async ({ request }) => {
  for (const f of ['fonts.css', 'fonts/space-grotesk-latin-400-normal.woff2', 'fonts/space-grotesk-latin-700-normal.woff2',
    'fonts/jetbrains-mono-latin-500-normal.woff2', 'fonts/playfair-display-latin-800-normal.woff',
    'fonts/source-sans-3-latin-400-normal.woff', 'fonts/source-sans-3-latin-700-normal.woff',
    'vendor/pdf-lib.min.js', 'vendor/fontkit.umd.min.js', 'img/vub-seal-360.png']) {
    const r = await request.get(`/courses/digital-literacy-2/os/${f}`);
    expect(r.status(), f).toBe(200);
  }
});

test('pdf-lib embeds the Playfair WOFF through fontkit', async () => {
  const { PDFDocument } = require(path.join(OS, 'vendor/pdf-lib.min.js'));
  const fontkit = require(path.join(OS, 'vendor/fontkit.umd.min.js'));
  const doc = await PDFDocument.create();
  doc.registerFontkit(fontkit);
  const font = await doc.embedFont(fs.readFileSync(path.join(OS, 'fonts/playfair-display-latin-800-normal.woff')));
  expect(font.widthOfTextAtSize('Veterans Upward Bound', 20)).toBeGreaterThan(100);
});
