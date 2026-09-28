/* DL2 graded-results PDF on the official letterhead (pdf-lib + fontkit, fonts self-hosted).
 * Letter size, 44pt margins. Items 1–10 on page 1, 11–20 plus signatures on page 2
 * (a 14/6 split overflowed page 1: the real item bank's wrapped answer text needs
 * up to ~492pt on a page with only ~435pt of table room; 10/10 leaves margin). */
(function (global) {
  'use strict';
  var here = (document.currentScript && document.currentScript.src) || location.href;
  var asset = function (p) { return new URL(p, here).href; };
  var NAVY = [27, 54, 93], GOLD = [201, 162, 39], RED = [179, 25, 66], INK = [21, 33, 58], MUTED = [91, 104, 131], RULE = [227, 232, 241], MISS = [253, 245, 246], OK = [29, 107, 58], NO = [163, 20, 47];
  var PW = 612, PH = 792, M = 44;

  function rgbOf(L, c) { return L.rgb(c[0] / 255, c[1] / 255, c[2] / 255); }
  function clean(s) { return String(s).replace(/▸/g, '>').replace(/[✓✗⚠]/g, '').replace(/[“”]/g, '"').replace(/[‘’]/g, "'"); }
  function fetchBytes(url) { return fetch(url).then(function (r) { if (!r.ok) throw new Error(url); return r.arrayBuffer(); }); }
  function wrap(font, text, size, width) {
    var words = clean(text).split(/\s+/), lines = [], line = '';
    words.forEach(function (w) {
      var t = line ? line + ' ' + w : w;
      if (font.widthOfTextAtSize(t, size) > width && line) { lines.push(line); line = w; } else line = t;
    });
    if (line) lines.push(line);
    return lines;
  }
  function spaced(s) { return s.split('').join(' '); }

  function build(report) {
    var L = global.PDFLib, META = global.DL2Paper.META;
    return L.PDFDocument.create().then(function (doc) {
      doc.registerFontkit(global.fontkit);
      var f = {};
      return Promise.all([
        /* { subset: true } is required: the vendored fontkit build throws
         * "Trying to access beyond buffer length" inside pdf-lib's default
         * whole-font embedder (it walks the font's entire character set at
         * save time and trips over a glyph outside what we actually draw).
         * Subsetting only touches the glyphs we use and avoids that path. */
        fetchBytes(asset('fonts/playfair-display-latin-800-normal.woff')).then(function (b) { return doc.embedFont(b, { subset: true }); }).catch(function () { return doc.embedFont(L.StandardFonts.TimesRomanBold); }),
        fetchBytes(asset('fonts/source-sans-3-latin-400-normal.woff')).then(function (b) { return doc.embedFont(b, { subset: true }); }).catch(function () { return doc.embedFont(L.StandardFonts.Helvetica); }),
        fetchBytes(asset('fonts/source-sans-3-latin-700-normal.woff')).then(function (b) { return doc.embedFont(b, { subset: true }); }).catch(function () { return doc.embedFont(L.StandardFonts.HelveticaBold); }),
        doc.embedFont(L.StandardFonts.Courier),
        fetchBytes(asset('img/vub-seal-360.png')).then(function (b) { return doc.embedPng(b); }).catch(function () { return null; })
      ]).then(function (res) {
        f.serif = res[0]; f.sans = res[1]; f.bold = res[2]; f.mono = res[3]; var seal = res[4];
        var r = report.result;
        doc.setTitle(report.recordId); doc.setSubject('DL2 ' + report.label + ' graded results');
        doc.setAuthor('West Virginia Veterans Upward Bound'); doc.setCreator('VUB Learning · DL2 Mission Control');
        doc.setCreationDate(report.submitted);

        var p1 = doc.addPage([PW, PH]), p2 = doc.addPage([PW, PH]);
        function text(p, s, x, y, size, font, color) { p.drawText(clean(s), { x: x, y: y, size: size, font: font, color: rgbOf(L, color || INK) }); }
        function right(p, s, xr, y, size, font, color) { text(p, s, xr - font.widthOfTextAtSize(clean(s), size), y, size, font, color); }
        function line(p, x1, y1, x2, y2, w, color) { p.drawLine({ start: { x: x1, y: y1 }, end: { x: x2, y: y2 }, thickness: w, color: rgbOf(L, color) }); }
        function box(p, x, y, w, h, fill, border) { p.drawRectangle({ x: x, y: y, width: w, height: h, color: fill ? rgbOf(L, fill) : undefined, borderColor: border ? rgbOf(L, border) : undefined, borderWidth: border ? 0.8 : 0 }); }

        function letterhead(p) {
          box(p, 0, PH - 8, PW * 0.6, 8, NAVY); box(p, PW * 0.6, PH - 8, PW * 0.2, 8, GOLD); box(p, PW * 0.8, PH - 8, PW * 0.2, 8, RED);
          if (seal) p.drawImage(seal, { x: M, y: PH - 116, width: 74, height: 74 });
          text(p, spaced(META.state), M + 88, PH - 58, 7.5, f.bold, [138, 109, 18]);
          text(p, META.org, M + 88, PH - 84, 21, f.serif, NAVY);
          text(p, META.trio, M + 88, PH - 100, 8.5, f.sans, MUTED);
          var mx = 392, my = PH - 56, rows = [['Course', META.course], ['Cohort', META.cohort], ['Instructor', META.instructor], ['Date & time', global.DL2Paper.classDate(report.submitted)], ['Location', META.location]];
          line(p, mx - 8, my + 10, mx - 8, my - 60, 1.6, GOLD);
          rows.forEach(function (row, k) { text(p, row[0], mx, my - k * 12.5, 7.5, f.bold, NAVY); text(p, row[1], mx + 50, my - k * 12.5, 7.5, f.sans, INK); });
          line(p, M, PH - 130, PW - M, PH - 130, 1.6, NAVY); line(p, M, PH - 134, PW - M, PH - 134, 0.7, GOLD);
        }
        function footer(p, n) {
          line(p, M, 40, PW - M, 40, 0.5, RULE);
          text(p, 'Page ' + n + ' of 2 · Record ' + report.recordId, M, 28, 7.5, f.sans, MUTED);
          right(p, 'Scores guide practice. They are not a certification.', PW - M, 28, 7.5, f.sans, MUTED);
        }
        function tableHead(p, y) {
          var cols = [[M, '#'], [M + 18, 'SKILL CHECKED'], [M + 212, 'YOUR ANSWER'], [M + 338, 'CORRECT ANSWER'], [M + 470, 'RESULT']];
          cols.forEach(function (c) { text(p, c[1], c[0], y, 6.8, f.bold, MUTED); });
          line(p, M, y - 5, PW - M, y - 5, 1.2, NAVY);
          return y - 7;
        }
        function row(p, y, rw) {
          var size = 8, lh = 10, skill = wrap(f.sans, rw.skill, size, 186), mine = wrap(f.sans, rw.chosen ? rw.chosen + ' · ' + rw.chosenText : 'Not answered', size, 118), key = wrap(f.sans, rw.answer + ' · ' + rw.answerText, size, 124);
          var n = Math.max(skill.length, mine.length, key.length), h = n * lh + 8;
          if (!rw.correct) box(p, M, y - h, PW - 2 * M, h, MISS);
          text(p, String(rw.n), M + 2, y - 12, size, f.bold, NAVY);
          skill.forEach(function (s, k) { text(p, s, M + 18, y - 12 - k * lh, size, f.sans); });
          mine.forEach(function (s, k) { text(p, s, M + 212, y - 12 - k * lh, size, f.sans); });
          key.forEach(function (s, k) { text(p, s, M + 338, y - 12 - k * lh, size, f.sans); });
          var ok = rw.correct, cx = M + 472, cy = y - 10;
          if (ok) { line(p, cx, cy, cx + 3, cy - 3, 1.3, OK); line(p, cx + 3, cy - 3, cx + 8, cy + 4, 1.3, OK); }
          else { line(p, cx, cy + 3, cx + 7, cy - 4, 1.3, NO); line(p, cx, cy - 4, cx + 7, cy + 3, 1.3, NO); }
          text(p, ok ? 'Correct' : 'Incorrect', cx + 12, y - 12, size, f.bold, ok ? OK : NO);
          line(p, M, y - h, PW - M, y - h, 0.5, RULE);
          return y - h;
        }

        // Page 1
        letterhead(p1);
        text(p1, report.label + ' · Graded Results', M, PH - 164, 17, f.serif, NAVY);
        right(p1, 'Record ' + report.recordId, PW - M, PH - 156, 7.5, f.mono, MUTED);
        right(p1, 'Form: ' + report.form + ' ' + global.DL2Items.version + ' · 20 items', PW - M, PH - 166, 7.5, f.mono, MUTED);
        var by = PH - 222, t = function (d) { return d.toLocaleTimeString('en-US', { hour: 'numeric', minute: '2-digit' }); };
        var mins = Math.max(1, Math.round((report.submitted - report.started) / 60000));
        box(p1, M, by, 190, 42, null, RULE); text(p1, 'STUDENT', M + 9, by + 28, 6.8, f.bold, MUTED); text(p1, report.name, M + 9, by + 12, 10.5, f.sans);
        box(p1, M + 198, by, 160, 42, null, RULE); text(p1, 'STARTED / SUBMITTED', M + 207, by + 28, 6.8, f.bold, MUTED); text(p1, t(report.started) + ' / ' + t(report.submitted) + ' (' + mins + ' min)', M + 207, by + 12, 9.5, f.sans);
        box(p1, M + 366, by, PW - 2 * M - 366, 42, NAVY); text(p1, r.correct + '/' + r.total, M + 378, by + 12, 22, f.serif, [255, 255, 255]);
        text(p1, 'SCORE', M + 452, by + 26, 6.8, f.bold, [201, 214, 238]); text(p1, r.percent + '% correct', M + 452, by + 12, 9.5, f.sans, [255, 255, 255]);
        var dy = by - 18;
        r.byDomain.forEach(function (d, k) {
          var col = k % 2, rowk = Math.floor(k / 2), x = M + col * 266, y = dy - rowk * 14;
          text(p1, d.name, x, y, 8, f.sans);
          box(p1, x + 128, y, 90, 6, RULE); box(p1, x + 128, y, 90 * (d.total ? d.correct / d.total : 0), 6, NAVY);
          right(p1, d.correct + '/' + d.total, x + 250, y, 8, f.bold, NAVY);
        });
        var y1 = tableHead(p1, dy - 70);
        r.rows.slice(0, 10).forEach(function (rw) { y1 = row(p1, y1, rw); });
        footer(p1, 1);

        // Page 2
        box(p2, 0, PH - 8, PW * 0.6, 8, NAVY); box(p2, PW * 0.6, PH - 8, PW * 0.2, 8, GOLD); box(p2, PW * 0.8, PH - 8, PW * 0.2, 8, RED);
        if (seal) p2.drawImage(seal, { x: M, y: PH - 76, width: 40, height: 40 });
        text(p2, META.org + ' · ' + report.label + ' · Graded Results (continued)', M + 50, PH - 58, 11, f.serif, NAVY);
        text(p2, report.name + ' · Record ' + report.recordId, M + 50, PH - 72, 8, f.sans, MUTED);
        line(p2, M, PH - 86, PW - M, PH - 86, 1.2, NAVY);
        var y2 = tableHead(p2, PH - 108);
        r.rows.slice(10).forEach(function (rw) { y2 = row(p2, y2, rw); });
        var sy = y2 - 90;
        line(p2, M, sy, M + 240, sy, 0.8, INK); text(p2, 'Student signature', M, sy - 12, 8, f.sans, MUTED); line(p2, M + 260, sy, M + 330, sy, 0.8, INK); text(p2, 'Date', M + 260, sy - 12, 8, f.sans, MUTED);
        line(p2, M, sy - 50, M + 240, sy - 50, 0.8, INK); text(p2, 'Instructor signature · ' + META.instructor, M, sy - 62, 8, f.sans, MUTED); line(p2, M + 260, sy - 50, M + 330, sy - 50, 0.8, INK); text(p2, 'Date', M + 260, sy - 62, 8, f.sans, MUTED);
        footer(p2, 2);
        return doc.save();
      });
    });
  }
  global.DL2Pdf = { build: build };
})(window);
