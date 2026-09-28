/* DL2 grading and record IDs. UMD so Node tests can require it. */
(function (global) {
  'use strict';
  var LETTERS = ['A', 'B', 'C', 'D'];
  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function initials(name) {
    var parts = String(name || '').trim().split(/\s+/).filter(Boolean);
    if (!parts.length) return 'X';
    return (parts[0][0] + (parts.length > 1 ? parts[parts.length - 1][0] : '')).toUpperCase();
  }
  function recordId(form, d, name) {
    return 'DL2-' + String(form).toUpperCase() + '-' + d.getFullYear() + pad(d.getMonth() + 1) + pad(d.getDate()) + '-' + pad(d.getHours()) + pad(d.getMinutes()) + '-' + initials(name);
  }
  function grade(items, answers) {
    var domains = (global.DL2Items || (typeof require === 'function' ? require('./items.js') : null)).domains;
    var byId = {};
    domains.forEach(function (d) { byId[d.id] = { id: d.id, name: d.name, correct: 0, total: 0 }; });
    var rows = items.map(function (it, i) {
      var chosen = answers[i] || null, ok = chosen === it.answer;
      byId[it.domain].total++; if (ok) byId[it.domain].correct++;
      return { n: it.n, skill: it.skill, chosen: chosen, chosenText: chosen ? it.options[LETTERS.indexOf(chosen)] : '', answer: it.answer, answerText: it.options[LETTERS.indexOf(it.answer)], correct: ok };
    });
    var correct = rows.filter(function (r) { return r.correct; }).length;
    return { correct: correct, total: items.length, percent: Math.round(100 * correct / items.length), byDomain: domains.map(function (d) { return byId[d.id]; }), rows: rows };
  }
  var api = { grade: grade, recordId: recordId, initials: initials, LETTERS: LETTERS };
  if (typeof module === 'object' && module.exports) module.exports = api; else global.DL2Grade = api;
})(typeof window !== 'undefined' ? window : globalThis);
