/* Renders DL2 answer keys and printable paper tests from the item bank. */
(function (global) {
  'use strict';
  var root = document.querySelector('[data-dl2-doc]');
  if (!root) return;
  var form = root.dataset.form === 'post' ? 'post' : 'pre', label = form === 'pre' ? 'Pre-Test' : 'Post-Test';
  var items = global.DL2Items[form], esc = global.DL2Paper.esc, L = ['A', 'B', 'C', 'D'];
  var dom = {}; global.DL2Items.domains.forEach(function (d) { dom[d.id] = d.name; });
  var head = global.DL2Paper.letterhead({ dateText: 'Class meeting · ' + global.DL2Paper.META.classTime });
  if (root.dataset.dl2Doc === 'key') {
    root.innerHTML = head + '<h1 class="doc-h1">' + label + ' · Answer Key <small>(instructor)</small></h1>' +
      '<p class="doc-sub">Form ' + form + ' ' + global.DL2Items.version + '. Item N checks the same skill on both forms.</p>' +
      '<table class="key"><thead><tr><th>#</th><th>Skill · domain</th><th>Answer</th><th>Why</th></tr></thead><tbody>' +
      items.map(function (it) {
        return '<tr><td>' + it.n + '</td><td>' + esc(it.skill) + '<br><small>' + dom[it.domain] + ' · Week ' + it.week + '</small></td><td><strong>' + it.answer + ' · ' + esc(it.options[L.indexOf(it.answer)]) + '</strong></td><td>' + esc(it.why) + '</td></tr>';
      }).join('') + '</tbody></table>';
  } else {
    root.innerHTML = head + '<h1 class="doc-h1">' + label + ' · Paper copy</h1>' +
      '<div class="namerow"><span>Name</span><span>Date</span></div>' +
      '<p class="doc-sub">Fill in one circle for each question. 20 questions.</p>' +
      items.map(function (it) {
        return '<section class="pq"><h2><b>' + it.n + '.</b> ' + esc(it.stem) + '</h2><div class="pq-opts">' +
          it.options.map(function (o, k) { return '<div class="pq-opt"><span class="bubble" aria-hidden="true">○</span><b>' + L[k] + '</b> ' + esc(o) + '</div>'; }).join('') + '</div></section>';
      }).join('');
  }
})(window);
