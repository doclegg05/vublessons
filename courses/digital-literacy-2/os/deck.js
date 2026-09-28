/* DL2 Mission Control deck engine.
 * One slide shows at a time. Next reveals the next .build part, then lets a registered
 * stepper (a Show demo) take a step, then moves to the next slide. Nothing auto-advances. */
(function (global) {
  'use strict';

  var PHASES = [['warm-up', 'Warm-up'], ['intro', 'Intro'], ['present', 'Present'], ['practice', 'Practice'], ['evaluate', 'Evaluate'], ['apply', 'Apply']];
  var STAGES = { tell: 'TELL', show: 'SHOW', do: 'DO', review: 'REVIEW' };
  var LEAVE_MS = 480;
  var GORGE_SVG = '<svg class="gorge-land" viewBox="0 0 1600 560" preserveAspectRatio="xMidYMax slice" aria-hidden="true"><defs>' +
    '<linearGradient id="dl2g1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7a3f80"/><stop offset="1" stop-color="#3a1f55"/></linearGradient>' +
    '<linearGradient id="dl2g2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3f2360"/><stop offset="1" stop-color="#1c1236"/></linearGradient>' +
    '<linearGradient id="dl2g3" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1d1233"/><stop offset="1" stop-color="#0b0718"/></linearGradient>' +
    '<linearGradient id="dl2gr" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffb36b" stop-opacity="0"/><stop offset=".5" stop-color="#ffd2a1" stop-opacity=".95"/><stop offset="1" stop-color="#ffb36b" stop-opacity="0"/></linearGradient></defs>' +
    '<path fill="url(#dl2g1)" d="M0 250 L120 190 L230 230 L360 150 L470 210 L600 170 L720 220 L860 140 L980 200 L1110 160 L1240 215 L1380 150 L1500 200 L1600 170 L1600 560 L0 560Z"/>' +
    '<path fill="url(#dl2g2)" d="M0 330 L140 260 L260 310 L400 240 L520 300 L660 250 L800 310 L940 270 L1060 330 L1100 360 L1100 560 L0 560Z M1310 360 L1350 320 L1450 280 L1600 300 L1600 560 L1310 560Z"/>' +
    '<path fill="url(#dl2gr)" d="M1080 478 Q1200 462 1330 478 L1330 487 Q1200 474 1080 487Z"/>' +
    '<g stroke="#150c28" fill="none" stroke-width="5" stroke-linecap="round"><path d="M950 330 L1450 330" stroke-width="7"/><path d="M1080 470 Q1200 230 1320 470" stroke-width="10"/>' +
    '<path d="M1100 330V433 M1125 330V397 M1150 330V371 M1175 330V355 M1200 330V350 M1225 330V355 M1250 330V371 M1275 330V397 M1300 330V433"/></g>' +
    '<path fill="url(#dl2g3)" d="M0 390 L110 350 L240 372 L380 340 L520 380 L660 350 L800 380 L940 340 L1040 360 L1085 470 L1085 560 L0 560Z M1315 470 L1360 350 L1450 372 L1530 345 L1600 360 L1600 560 L1315 560Z"/></svg>';

  var deck, slides = [], index = 0, steppers = new Map(), ui = {}, typed = '';
  var timer = { left: 0, total: 0, running: false, expired: false, handle: null };
  var storeKey = 'dl2os:slide:' + location.pathname;

  /* The resume position lives in sessionStorage: a reload (or reopening the deck in the same tab)
   * keeps its place, but a fresh browser opens at slide 1, so a rehearsal on the presenting PC
   * never makes class start mid-deck. */
  function safeGet(key) { try { return sessionStorage.getItem(key); } catch (e) { return null; } }
  function safeSet(key, value) { try { sessionStorage.setItem(key, value); } catch (e) { /* storage blocked */ } }

  function parts(slide) { return Array.prototype.slice.call(slide.querySelectorAll('.build')); }
  function shown(slide) { return Number(slide.dataset.step || 0); }
  function setStep(slide, n) {
    var list = parts(slide);
    n = Math.max(0, Math.min(list.length, n));
    list.forEach(function (el, k) { el.classList.toggle('on', k < n); el.classList.toggle('now', k === n - 1); });
    slide.dataset.step = String(n);
    slide.dataset.steps = String(list.length);
  }

  function pad(n) { return (n < 10 ? '0' : '') + n; }
  function renderTimer() {
    var seg = ui.timer;
    seg.classList.toggle('expired', timer.expired);
    seg.classList.toggle('running', timer.running);
    seg.textContent = timer.expired ? "TIME'S UP" : timer.total ? 'T-' + pad(Math.floor(timer.left / 60)) + ':' + pad(timer.left % 60) : 'T--:--';
  }
  function stopTimer() { timer.running = false; clearInterval(timer.handle); timer.handle = null; }
  function setTimer(minutes) { stopTimer(); timer.total = timer.left = Math.round(minutes * 60); timer.expired = false; renderTimer(); }
  function toggleTimer() {
    if (!timer.total || timer.expired) return;
    if (timer.running) { stopTimer(); renderTimer(); return; }
    timer.running = true;
    timer.handle = setInterval(function () {
      timer.left = Math.max(0, timer.left - 1);
      if (timer.left === 0) { stopTimer(); timer.expired = true; }
      renderTimer();
    }, 1000);
    renderTimer();
  }

  function renderChrome() {
    var slide = slides[index];
    var at = PHASES.map(function (p) { return p[0]; }).indexOf(slide.dataset.phase || '');
    ui.segs.forEach(function (seg, k) {
      seg.classList.toggle('done', at > -1 && k < at);
      seg.classList.toggle('now', k === at);
      if (k === at) seg.setAttribute('aria-current', 'step'); else seg.removeAttribute('aria-current');
    });
    ui.count.textContent = (index + 1) + ' / ' + slides.length;
    var note = slide.querySelector('.notes');
    ui.notes.innerHTML = '<h2>Notes · slide ' + (index + 1) + '</h2>' + (note ? note.innerHTML : '<p>No notes for this slide.</p>');
    document.body.setAttribute('data-scene', slide.dataset.scene || 'deck');
  }

  function go(to, dir) {
    to = Math.max(0, Math.min(slides.length - 1, to));
    var old = slides[index], next = slides[to];
    if (old !== next) {
      old.classList.remove('is-active');
      old.classList.add('is-leaving');
      old.setAttribute('aria-hidden', 'true');
      old.inert = true;
      setTimeout(function () { old.classList.remove('is-leaving'); }, LEAVE_MS);
    }
    index = to;
    next.classList.add('is-active');
    next.removeAttribute('aria-hidden');
    next.inert = false;
    setStep(next, dir === 'back' ? parts(next).length : 0);
    var stepper = steppers.get(next);
    if (stepper) stepper.reset();
    if (next.dataset.minutes) setTimer(Number(next.dataset.minutes));
    renderChrome();
    safeSet(storeKey, String(index));
    if (history.replaceState) history.replaceState(null, '', '#' + (index + 1));
    document.dispatchEvent(new CustomEvent('dl2:slide', { detail: { index: index, slide: next } }));
  }

  function next() {
    var slide = slides[index];
    if (shown(slide) < parts(slide).length) { setStep(slide, shown(slide) + 1); return; }
    var stepper = steppers.get(slide);
    if (stepper && stepper.next()) return;
    if (index < slides.length - 1) go(index + 1, 'forward');
  }
  function prev() {
    var slide = slides[index];
    var stepper = steppers.get(slide);
    if (stepper && stepper.back()) return;
    if (shown(slide) > 0) { setStep(slide, shown(slide) - 1); return; }
    if (index > 0) go(index - 1, 'back');
  }

  function toggleNotes() { ui.notes.hidden = !ui.notes.hidden; }
  function toggleFullscreen() {
    if (document.fullscreenElement) document.exitFullscreen();
    else if (document.documentElement.requestFullscreen) document.documentElement.requestFullscreen().catch(function () {});
  }

  function onKey(e) {
    if (e.defaultPrevented || e.altKey || e.ctrlKey || e.metaKey) return;
    var t = e.target, tag = t && t.tagName;
    if (tag === 'INPUT' || tag === 'TEXTAREA' || tag === 'SELECT' || (t && t.isContentEditable)) return;
    var onControl = tag === 'BUTTON' || tag === 'A';
    var k = e.key;
    if (/^[0-9]$/.test(k)) { typed += k; return; }
    if (k === 'Enter' && typed) { e.preventDefault(); go(Number(typed) - 1, 'forward'); typed = ''; return; }
    typed = '';
    if (k === 'ArrowRight' || k === 'PageDown' || (k === ' ' && !onControl)) { e.preventDefault(); next(); }
    else if (k === 'ArrowLeft' || k === 'PageUp' || k === 'Backspace') { e.preventDefault(); prev(); }
    else if (k === 'Home') { e.preventDefault(); go(0, 'forward'); }
    else if (k === 'End') { e.preventDefault(); go(slides.length - 1, 'forward'); }
    else if (k === 'n' || k === 'N') toggleNotes();
    else if (k === 't' || k === 'T') toggleTimer();
    else if (k === 'f' || k === 'F') toggleFullscreen();
    else if (k === 'b' || k === 'B' || k === '.') document.body.classList.toggle('blackout');
  }

  function onSwipe() {
    var x0 = null;
    deck.addEventListener('pointerdown', function (e) { if (e.pointerType === 'touch') x0 = e.clientX; });
    deck.addEventListener('pointerup', function (e) {
      if (x0 === null) return;
      var dx = e.clientX - x0; x0 = null;
      if (dx < -60) next(); else if (dx > 60) prev();
    });
  }

  function buildChrome() {
    var scenes = document.createElement('div');
    scenes.className = 'scenes';
    scenes.setAttribute('aria-hidden', 'true');
    scenes.innerHTML = '<div class="scene scene-deck"><div class="grid"></div></div>' +
      '<div class="scene scene-gorge"><div class="stars"></div><div class="sun"></div>' + GORGE_SVG + '</div>';
    document.body.insertBefore(scenes, document.body.firstChild);

    var strip = document.createElement('nav');
    strip.className = 'strip';
    strip.setAttribute('aria-label', 'Lesson phase');
    ui.segs = PHASES.map(function (p) {
      var s = document.createElement('span');
      s.className = 'seg'; s.dataset.phase = p[0]; s.textContent = p[1];
      strip.appendChild(s);
      return s;
    });
    ui.timer = document.createElement('span'); ui.timer.className = 'seg t'; ui.timer.setAttribute('role', 'timer'); strip.appendChild(ui.timer);
    ui.count = document.createElement('span'); ui.count.className = 'seg count'; strip.appendChild(ui.count);
    var host = document.createElement('span');
    host.className = 'seg vub-appbar';
    host.innerHTML = '<span class="vub-textsize" role="group" aria-label="Text size"><button type="button" data-vub-textsize-minus aria-label="Decrease text size">A−</button><button type="button" data-vub-textsize-plus aria-label="Increase text size">A+</button></span>';
    strip.appendChild(host);
    deck.appendChild(strip);

    ui.notes = document.createElement('aside');
    ui.notes.className = 'notes-panel';
    ui.notes.hidden = true;
    document.body.appendChild(ui.notes);
    renderTimer();
  }

  function tagStages() {
    slides.forEach(function (s) {
      var label = STAGES[s.dataset.stage], hud = s.querySelector('.hud');
      if (label && hud && !hud.querySelector('.tag')) {
        var tag = document.createElement('span');
        tag.className = 'tag tag-' + s.dataset.stage; tag.textContent = label;
        hud.appendChild(tag);
      }
    });
  }

  function init() {
    deck = document.querySelector('.deck');
    if (!deck) return;
    slides = Array.prototype.slice.call(deck.querySelectorAll('.slide'));
    if (!slides.length) return;
    slides.forEach(function (s) { s.setAttribute('aria-hidden', 'true'); s.inert = true; setStep(s, 0); });
    tagStages();
    buildChrome();
    var fromHash = parseInt((location.hash || '').slice(1), 10);
    var saved = parseInt(safeGet(storeKey) || '', 10);
    var start = fromHash > 0 ? fromHash - 1 : (saved >= 0 ? saved : 0);
    index = 0;
    go(isNaN(start) ? 0 : start, 'forward');
    document.addEventListener('keydown', onKey);
    onSwipe();
  }

  global.DL2Deck = {
    go: go, next: next, prev: prev,
    index: function () { return index; },
    count: function () { return slides.length; },
    registerStepper: function (slide, stepper) { steppers.set(slide, stepper); if (slide === slides[index]) stepper.reset(); }
  };
  init();
})(window);
