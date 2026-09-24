/* Progressive enhancement: retain each deck's authored slide navigation. */
(function () {
  'use strict';
  function init() {
    var sidebar = document.querySelector('.sidebar');
    if (!sidebar) return;
    sidebar.id = 'ics-lesson-navigation';
    var toolbar = document.createElement('div');
    toolbar.className = 'ics-toolbar';
    toolbar.innerHTML = '<button class="ics-menu-toggle" type="button" aria-controls="ics-lesson-navigation" aria-expanded="false">Lesson menu</button><a class="ics-course-link" href="/courses/computer-skills/">Computer Skills course home</a>';
    document.body.prepend(toolbar);
    var toggle = toolbar.querySelector('button');
    var smallScreen = window.matchMedia('(max-width: 900px)');
    function setOpen(open, returnFocus) {
      sidebar.hidden = smallScreen.matches && !open;
      toggle.setAttribute('aria-expanded', String(!sidebar.hidden));
      if (returnFocus && smallScreen.matches) toggle.focus();
    }
    toggle.addEventListener('click', function () { setOpen(sidebar.hidden); });
    smallScreen.addEventListener('change', function () { setOpen(!smallScreen.matches); });
    setOpen(!smallScreen.matches);
    sidebar.addEventListener('click', function (event) {
      if (event.target.closest('.slide-link, .slide-item') && smallScreen.matches) setOpen(false, true);
    });
    // The old global shortcuts must not consume Space on a button, or Home/End
    // in an input. Let native activation and text editing retain their meaning.
    document.addEventListener('keydown', function (event) {
      if (event.key === 'Escape' && smallScreen.matches && !sidebar.hidden && !event.target.closest('[role="dialog"]')) {
        setOpen(false, true);
        event.preventDefault();
        event.stopImmediatePropagation();
        return;
      }
      if ([' ', 'ArrowLeft', 'ArrowRight', 'PageUp', 'PageDown', 'Home', 'End'].includes(event.key) && event.target.closest('button, a, input, textarea, select, [contenteditable="true"], .ics-table-scroll')) {
        event.stopImmediatePropagation();
      } else if (['ArrowLeft', 'ArrowRight', 'PageUp', 'PageDown', 'Home', 'End'].includes(event.key)) {
        event.preventDefault();
      }
    }, true);
    // Preserve tabular relationships with a keyboard-scrollable local viewport.
    document.querySelectorAll('.slide table').forEach(function (table) {
      var wrapper = document.createElement('div');
      wrapper.className = 'ics-table-scroll';
      wrapper.tabIndex = 0;
      wrapper.setAttribute('role', 'region');
      wrapper.setAttribute('aria-label', 'Lesson table. Scroll horizontally to see all columns.');
      table.before(wrapper);
      wrapper.appendChild(table);
    });
    // The global text-size module creates its control on the next event tick.
    setTimeout(function () {
      var control = document.querySelector('.vub-textsize-fab');
      if (control) toolbar.appendChild(control);
      var help = document.querySelector('.vub-help-fab');
      if (help) toolbar.appendChild(help);
    }, 0);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
