/* DL2 pre/post test: name → 20 questions → review → submit → grade → PDF → copy to Britt.
 * Answers survive a reload. If sending fails, the copy waits in an outbox and retries next visit. */
(function (global) {
  'use strict';
  var root = document.querySelector('[data-dl2-test]');
  if (!root) return;
  var FORM = root.dataset.form === 'post' ? 'post' : 'pre';
  var LABEL = FORM === 'pre' ? 'Pre-Test' : 'Post-Test';
  var ITEMS = global.DL2Items[FORM];
  var KEY = 'dl2os:test:' + FORM, OUTBOX = 'dl2os:outbox';
  var LETTERS = ['A', 'B', 'C', 'D'];
  var esc = global.DL2Paper.esc;
  var st = load() || { phase: 'start', name: '', started: null, at: 0, answers: ITEMS.map(function () { return null; }) };

  function load() { try { return JSON.parse(localStorage.getItem(KEY)); } catch (e) { return null; } }
  function save() { try { localStorage.setItem(KEY, JSON.stringify(st)); } catch (e) { /* storage blocked */ } }
  function clear() { try { localStorage.removeItem(KEY); } catch (e) { /* storage blocked */ } }
  function readOutbox() { try { return JSON.parse(localStorage.getItem(OUTBOX) || '[]'); } catch (e) { return []; } }
  function writeOutbox(list) { try { localStorage.setItem(OUTBOX, JSON.stringify(list)); } catch (e) { /* storage blocked */ } }

  function top(extra) {
    return '<header class="test-top"><img src="/courses/digital-literacy-2/os/img/vub-seal-360.png" alt="" width="44" height="44">' +
      '<div class="ttl">Digital Literacy Level 2 · ' + LABEL + (st.name ? '<small>' + esc(st.name) + '</small>' : '') + '</div>' +
      (extra || '') + '</header>';
  }
  function ticks() {
    return '<div class="ticks" aria-hidden="true">' + ITEMS.map(function (_, i) {
      return '<i class="' + (st.answers[i] ? 'a' : '') + (i === st.at ? ' c' : '') + '"></i>';
    }).join('') + '</div>';
  }

  function renderStart(error) {
    root.innerHTML = top() + '<main class="test-card start" id="main"><h1>' + LABEL + '</h1>' +
      '<p>20 questions · about 20 minutes. Pick the best answer for each. You can go back and change answers before you submit.</p>' +
      '<p>' + (FORM === 'pre' ? 'This shows where to start. It is not a grade.' : 'This shows how far you’ve come since the pre-test.') + '</p>' +
      '<label for="name">Your full name</label><input id="name" autocomplete="name" value="' + esc(st.name) + '">' +
      (error ? '<p class="field-error" role="alert">' + error + '</p>' : '') +
      '<div class="test-nav"><span></span><button type="button" class="primary" data-go="begin">Start the ' + LABEL.toLowerCase() + '</button></div></main>';
    root.querySelector('#name').focus();
  }

  function renderQuestion() {
    var it = ITEMS[st.at], chosen = st.answers[st.at];
    root.innerHTML = top('<div class="q-count">Question ' + (st.at + 1) + ' of 20</div>') + ticks() +
      '<main class="test-card" id="main"><h1 class="q" id="q-stem">' + esc(it.stem) + '</h1><div class="opts" role="radiogroup" aria-labelledby="q-stem">' +
      it.options.map(function (o, k) {
        var L = LETTERS[k], on = chosen === L;
        return '<button type="button" class="opt' + (on ? ' sel' : '') + '" role="radio" aria-checked="' + on + '" data-letter="' + L + '"><b>' + L + '</b><span>' + esc(o) + '</span><span class="pick">' + (on ? '✓ Selected' : '') + '</span></button>';
      }).join('') + '</div>' +
      '<div class="test-nav"><button type="button" data-go="back"' + (st.at === 0 ? ' disabled' : '') + '>◀ Back</button>' +
      '<button type="button" class="primary" data-go="next">' + (st.at === 19 ? 'Review answers' : 'Next ▶') + '</button></div></main>';
    var sel = root.querySelector('.opt.sel') || root.querySelector('.opt');
    sel.focus();
  }

  function renderReview() {
    var answered = st.answers.filter(Boolean).length;
    root.innerHTML = top('<div class="q-count">Review</div>') + '<main class="test-card" id="main"><h1 tabindex="-1">Check your answers</h1>' +
      '<p>You answered <strong>' + answered + ' of 20</strong>. Select any question to change it.</p><div class="review">' +
      ITEMS.map(function (it, i) {
        var a = st.answers[i];
        return '<button type="button" class="review-row' + (a ? '' : ' skipped') + '" data-jump="' + i + '"><b>' + (i + 1) + '</b><span>' + esc(it.stem) + '</span><em>' + (a ? 'Answer: ' + a : '⚠ Not answered') + '</em></button>';
      }).join('') + '</div><div class="test-nav"><button type="button" data-go="last">◀ Back to question 20</button><button type="button" class="primary" data-go="submit">Submit my test</button></div>' +
      '<dialog class="confirm"><h2>Submit your test?</h2><p>You answered ' + answered + ' of 20. You can’t change answers after you submit.</p>' +
      '<div class="test-nav"><button type="button" data-go="cancel">Go back</button><button type="button" class="primary" data-go="confirm">Yes, submit</button></div></dialog></main>';
    root.querySelector('main h1').focus();
  }

  function download(bytes, filename) {
    var url = URL.createObjectURL(new Blob([bytes], { type: 'application/pdf' }));
    var a = document.createElement('a'); a.href = url; a.download = filename; document.body.appendChild(a); a.click(); a.remove();
    return url;
  }
  function send(payload) {
    var body = new URLSearchParams(payload).toString();
    return fetch('/', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: body })
      .then(function (r) { if (!r.ok) throw new Error('HTTP ' + r.status); return true; });
  }
  /* Outbox writes always re-read from storage immediately before writing, so a write
   * here never clobbers an item another code path (a fresh submission failure, or a
   * concurrent flush) added or removed in the meantime. */
  function enqueueOutbox(item) {
    var list = readOutbox().filter(function (i) { return i['record-id'] !== item['record-id']; });
    list.push(item);
    writeOutbox(list);
  }
  function dequeueOutbox(recordId) {
    var list = readOutbox().filter(function (i) { return i['record-id'] !== recordId; });
    writeOutbox(list);
  }
  function flushOutbox() {
    var list = readOutbox();
    if (!list.length) return;
    list.reduce(function (p, item) {
      return p.then(function () {
        return send(item).then(function () {
          dequeueOutbox(item['record-id']);
        }).catch(function () { /* leave it queued; retried on the next flush */ });
      });
    }, Promise.resolve());
  }

  function submit() {
    var submitted = new Date(), started = new Date(st.started);
    var result = global.DL2Grade.grade(ITEMS, st.answers);
    var rid = global.DL2Grade.recordId(FORM, submitted, st.name);
    var payload = {
      'form-name': 'dl2-' + FORM + 'test', 'bot-field': '', 'record-id': rid, student: st.name, form: FORM + ' ' + global.DL2Items.version,
      started: started.toISOString(), submitted: submitted.toISOString(), score: result.correct + '/' + result.total,
      domains: result.byDomain.map(function (d) { return d.id + ':' + d.correct + '/' + d.total; }).join(' '),
      answers: st.answers.map(function (a) { return a || '-'; }).join(',')
    };
    var report = { form: FORM, label: LABEL, items: ITEMS, result: result, name: st.name, started: started, submitted: submitted, recordId: rid };
    clear();
    renderResult(report, payload);
  }

  function renderResult(report, payload) {
    var r = report.result, last = String(report.name).trim().split(/\s+/).pop().replace(/[^A-Za-z0-9-]/g, '') || 'Student';
    var filename = 'DL2-' + report.label.replace('-', '') + '-' + last + '-' + report.recordId.split('-').slice(2, 4).join('-') + '.pdf';
    root.innerHTML = top() + '<main class="test-card result" id="main"><h1 tabindex="-1">Thank you, ' + esc(report.name) + '!</h1>' +
      '<p class="result-score">' + r.correct + ' of 20 correct</p><p class="pdf-status" role="status">Making your results PDF…</p>' +
      '<p class="copy-status" role="status">Sending a copy to Britt…</p>' +
      '<div class="test-nav"><button type="button" data-go="pdf" disabled>Save my PDF again</button><button type="button" class="primary" data-go="print" disabled>Print my results</button></div>' +
      '<div class="html-report" hidden></div></main>';
    root.querySelector('main h1').focus();
    var pdfUrl = null, bytes = null;
    var build = global.DL2Pdf ? global.DL2Pdf.build(report) : Promise.reject(new Error('PDF library not loaded'));
    build.then(function (b) {
      bytes = b; pdfUrl = download(bytes, filename);
      root.querySelector('.pdf-status').textContent = 'Your PDF is saved in Downloads as ' + filename + '.';
      root.querySelectorAll('[data-go="pdf"],[data-go="print"]').forEach(function (btn) { btn.disabled = false; });
    }).catch(function (err) {
      console.error('DL2 PDF failed', err);
      root.querySelector('.pdf-status').textContent = 'The PDF could not be made on this computer. Your full report is below. Use Print.';
      var box = root.querySelector('.html-report'); box.hidden = false; box.innerHTML = htmlReport(report);
      root.querySelector('[data-go="print"]').disabled = false;
    });
    root.addEventListener('click', function (e) {
      var go = e.target.closest('[data-go]'); if (!go) return;
      if (go.dataset.go === 'pdf' && bytes) download(bytes, filename);
      if (go.dataset.go === 'print') { if (pdfUrl) global.open(pdfUrl, '_blank'); else global.print(); }
    });
    send(payload).then(function () {
      root.querySelector('.copy-status').textContent = '✓ A copy was sent to Britt.';
    }).catch(function () {
      enqueueOutbox(payload);
      root.querySelector('.copy-status').textContent = 'Saved on this computer. Tell Britt.';
    });
  }

  function htmlReport(report) {
    var r = report.result;
    return '<div class="paper-doc">' + global.DL2Paper.letterhead({ date: report.submitted }) +
      '<h2>' + report.label + ' · Graded Results</h2><p>Record ' + report.recordId + ' · ' + esc(report.name) + ' · ' + r.correct + '/20</p>' +
      '<table><thead><tr><th>#</th><th>Skill checked</th><th>Your answer</th><th>Correct answer</th><th>Result</th></tr></thead><tbody>' +
      r.rows.map(function (row) {
        return '<tr' + (row.correct ? '' : ' class="miss"') + '><td>' + row.n + '</td><td>' + esc(row.skill) + '</td><td>' + (row.chosen ? row.chosen + ' · ' + esc(row.chosenText) : 'Not answered') + '</td><td>' + row.answer + ' · ' + esc(row.answerText) + '</td><td>' + (row.correct ? '✓ Correct' : '✗ Incorrect') + '</td></tr>';
      }).join('') + '</tbody></table></div>';
  }

  function render() {
    if (st.phase === 'start') renderStart();
    else if (st.phase === 'q') renderQuestion();
    else if (st.phase === 'review') renderReview();
  }

  root.addEventListener('click', function (e) {
    var opt = e.target.closest('.opt');
    if (opt) { st.answers[st.at] = opt.dataset.letter; save(); renderQuestion(); return; }
    var jump = e.target.closest('[data-jump]');
    if (jump) { st.at = Number(jump.dataset.jump); st.phase = 'q'; save(); render(); return; }
    var go = e.target.closest('[data-go]'); if (!go) return;
    var act = go.dataset.go;
    if (act === 'begin') {
      var name = root.querySelector('#name').value.trim().replace(/\s+/g, ' ');
      if (name.length < 2) return renderStart('Please type your name so your results are yours.');
      st.name = name; st.started = new Date().toISOString(); st.phase = 'q'; st.at = 0; save(); render();
    } else if (act === 'next') { if (st.at === 19) st.phase = 'review'; else st.at++; save(); render(); }
    else if (act === 'back') { st.at = Math.max(0, st.at - 1); save(); render(); }
    else if (act === 'last') { st.phase = 'q'; st.at = 19; save(); render(); }
    else if (act === 'submit') root.querySelector('dialog.confirm').showModal();
    else if (act === 'cancel') {
      root.querySelector('dialog.confirm').close();
      var submitBtn = root.querySelector('[data-go="submit"]');
      if (submitBtn) submitBtn.focus();
    }
    else if (act === 'confirm') { root.querySelector('dialog.confirm').close(); submit(); }
  });
  root.addEventListener('keydown', function (e) {
    if (st.phase !== 'q') return;
    if (e.target.matches('input')) return;
    var k = e.key.toUpperCase();
    if (LETTERS.indexOf(k) > -1) { st.answers[st.at] = k; save(); renderQuestion(); return; }
    /* ARIA radiogroup keyboard pattern: Down/Right moves to (and selects) the next
     * option, Up/Left the previous one, wrapping at the ends. Selection follows focus,
     * matching the letter-key and click behaviors above. */
    var dir = (e.key === 'ArrowDown' || e.key === 'ArrowRight') ? 1 : (e.key === 'ArrowUp' || e.key === 'ArrowLeft') ? -1 : 0;
    if (!dir) return;
    e.preventDefault();
    var count = ITEMS[st.at].options.length;
    var idx = LETTERS.indexOf(st.answers[st.at]);
    var nextIdx = idx === -1 ? (dir === 1 ? 0 : count - 1) : (idx + dir + count) % count;
    st.answers[st.at] = LETTERS[nextIdx]; save(); renderQuestion();
  });

  flushOutbox();
  render();
  global.DL2Test = { state: function () { return st; } };
})(window);
