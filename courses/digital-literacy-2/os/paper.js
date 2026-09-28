/* DL2 paper system: the official letterhead used by the graded report, answer keys,
 * printable tests and (as static copies) the worksheets. */
(function (global) {
  'use strict';
  var META = {
    state: 'WEST VIRGINIA', org: 'Veterans Upward Bound', trio: 'A TRIO program funded by the U.S. Department of Education',
    course: 'Digital Literacy Level 2', cohort: 'Fall 2026 · Sep 28 – Nov 2', instructor: 'Britt Legg',
    location: 'New River Community and Technical College', classTime: '4:30–6:30 PM ET'
  };
  function classDate(d) { return d.toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric', year: 'numeric', timeZone: 'America/New_York' }) + ' · ' + META.classTime; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function letterhead(opts) {
    var date = opts && opts.date ? classDate(opts.date) : (opts && opts.dateText) || '';
    var seal = (opts && opts.seal) || '/courses/digital-literacy-2/os/img/vub-seal-360.png';
    return '<header class="letterhead"><div class="lh-bar" aria-hidden="true"></div>' +
      '<img class="lh-seal" src="' + seal + '" alt="Veterans Upward Bound seal">' +
      '<div class="lh-org"><div class="lh-state">' + META.state + '</div><div class="lh-name">' + META.org + '</div><div class="lh-trio">' + META.trio + '</div></div>' +
      '<dl class="lh-meta"><div><dt>Course</dt><dd>' + META.course + '</dd></div><div><dt>Cohort</dt><dd>' + META.cohort + '</dd></div>' +
      '<div><dt>Instructor</dt><dd>' + META.instructor + '</dd></div><div><dt>Date &amp; time</dt><dd>' + esc(date) + '</dd></div>' +
      '<div><dt>Location</dt><dd>' + META.location + '</dd></div></dl><div class="lh-rule" aria-hidden="true"></div></header>';
  }
  var api = { META: META, classDate: classDate, letterhead: letterhead, esc: esc };
  if (typeof module === 'object' && module.exports) module.exports = api; else global.DL2Paper = api;
})(typeof window !== 'undefined' ? window : globalThis);
