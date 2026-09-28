(function () {
  'use strict';
  document.querySelectorAll('[data-print]').forEach(function (b) { b.addEventListener('click', function () { window.print(); }); });
  document.querySelectorAll('textarea').forEach(function (field) {
    // Session-only work on shared lab PCs. Printing retains the typed evidence.
    var key = 'dl2-mission-paper:' + location.pathname + ':' + field.id;
    try { field.value = sessionStorage.getItem(key) || ''; } catch (_) {}
    function sync() { var out = field.nextElementSibling; if (out && out.classList.contains('print-answer')) out.textContent = field.value; }
    sync();
    field.addEventListener('input', function () { sync(); try { sessionStorage.setItem(key, field.value); } catch (_) {} });
  });
})();
