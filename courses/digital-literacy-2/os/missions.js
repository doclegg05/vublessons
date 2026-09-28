/* Scoped progressive enhancement: native buttons, local feedback, no network/submission. */
(function () {
  'use strict';
  function init() {
    var deck = window.DL2Deck;
    if (!deck) return;
    document.querySelector('[data-deck-next]').addEventListener('click', deck.next);
    document.querySelector('[data-deck-prev]').addEventListener('click', deck.prev);
    document.querySelector('[data-mission-jump]').addEventListener('change', function (e) { deck.go(Number(e.target.value), 'forward'); });
    var notesButton = document.querySelector('[data-deck-notes]');
    function shortcut(key) { document.dispatchEvent(new KeyboardEvent('keydown', { key: key, bubbles: true })); }
    notesButton.addEventListener('click', function () { shortcut('n'); });
    document.querySelector('[data-deck-full]').addEventListener('click', function () { shortcut('f'); });
    function syncNavigation() {
      var at = deck.index(), starts = Array.from(document.querySelector('[data-mission-jump]').options).map(function (o) { return Number(o.value); }), mission = 0;
      starts.forEach(function (start) { if (at >= start) mission = start; });
      document.querySelector('[data-mission-jump]').value = String(mission);
      document.querySelector('[data-deck-prev]').disabled = at === 0;
      document.querySelector('[data-deck-next]').disabled = at === deck.count() - 1;
    }
    new MutationObserver(syncNavigation).observe(document.querySelector('.strip .count'), { childList: true });
    syncNavigation();
    var notes = document.querySelector('.notes-panel');
    new MutationObserver(function () { notesButton.setAttribute('aria-expanded', String(!notes.hidden)); }).observe(notes, { attributes: true, attributeFilter: ['hidden'] });
    document.querySelectorAll('[data-mission-demo]').forEach(function (host) {
      var states = Array.from(host.querySelectorAll('[data-state]')), at = 0;
      function show(i) {
        at = i;
        states.forEach(function (state, n) { state.hidden = n !== at; });
        host.querySelector('.demo-count').textContent = 'Step ' + (at + 1) + ' of ' + states.length;
        host.querySelector('[data-demo-back]').disabled = at === 0;
        host.querySelector('[data-demo-next]').disabled = at === states.length - 1;
      }
      var controller = { next: function () { if (at >= states.length - 1) return false; show(at + 1); return true; }, back: function () { if (at === 0) return false; show(at - 1); return true; }, reset: function () { show(0); } };
      host.querySelector('[data-demo-next]').addEventListener('click', controller.next);
      host.querySelector('[data-demo-back]').addEventListener('click', controller.back);
      host.querySelector('[data-demo-reset]').addEventListener('click', controller.reset);
      deck.registerStepper(host.closest('.slide'), controller);show(0);
    });
    document.querySelectorAll('.mission-check').forEach(function (host) {
      var choices = Array.from(host.querySelectorAll('[data-choice]')), status = host.querySelector('[role="status"]');
      choices.forEach(function (button) {
        button.setAttribute('aria-pressed', 'false');
        button.addEventListener('click', function () {
          choices.forEach(function (b) { b.setAttribute('aria-pressed', String(b === button)); });
          status.textContent = (button.dataset.choice === host.dataset.answer ? 'Correct. ' : 'Reconsider. ') + host.dataset.why;
        });
      });
      host.querySelector('.check-reset').addEventListener('click', function () { choices.forEach(function (b) { b.setAttribute('aria-pressed', 'false'); }); status.textContent = 'Choose an answer, then explain your reason.'; choices[0].focus(); });
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
