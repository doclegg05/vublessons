/* DL2 Show engine: plays a Windows 11 recreation one step at a time with a guided cursor,
 * camera zoom, spotlight and click ripple. States are cumulative, so Back rebuilds instantly. */
(function (global) {
  'use strict';
  var W = 1280, H = 720;
  /* Camera pacing (Britt, 2026-09-28): slow, gentle and at most one move per step, so viewers stay oriented. */
  var CAM_MS = 1400, CURSOR_MS = 1000, CAM_EASE = 'cubic-bezier(.4,0,.2,1)', ZOOM = 1.5, MAX_ZOOM = 1.8;
  var registry = {}, controllers = {};
  var reduce = !!(global.matchMedia && global.matchMedia('(prefers-reduced-motion: reduce)').matches);
  var CURSOR = '<svg viewBox="0 0 22 30" aria-hidden="true"><path d="M1.5 1.5 L1.5 23 L7 17.8 L10.8 27 L14.4 25.5 L10.7 16.5 L18 16.5 Z" fill="#fff" stroke="#000" stroke-width="1.6" stroke-linejoin="round"/></svg>';

  function define(def) { registry[def.id] = def; return def; }
  function make(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }

  function applyState(screen, st) {
    if (!st) return;
    Object.keys(st.attr || {}).forEach(function (k) { screen.setAttribute('data-' + k, st.attr[k]); });
    Object.keys(st.cls || {}).forEach(function (k) { screen.classList.toggle(k, !!st.cls[k]); });
    Object.keys(st.text || {}).forEach(function (sel) { screen.querySelectorAll(sel).forEach(function (n) { n.textContent = st.text[sel]; }); });
    Object.keys(st.css || {}).forEach(function (k) { screen.style.setProperty(k, st.css[k]); });
  }
  function offset(el, root) {
    var x = 0, y = 0, e = el;
    while (e && e !== root) { x += e.offsetLeft; y += e.offsetTop; e = e.offsetParent; }
    return { x: x, y: y, w: el.offsetWidth, h: el.offsetHeight };
  }

  function mount(host) {
    var def = registry[host.dataset.demo];
    if (!def) { console.error('DL2Demo: no demo named', host.dataset.demo); return null; }
    host.innerHTML = '';
    host.classList.add('demo');
    var bezel = make('div', 'demo-bezel'), vp = make('div', 'demo-viewport');
    bezel.setAttribute('role', 'img');
    bezel.setAttribute('aria-label', 'Windows 11 demonstration: ' + def.title);
    bezel.appendChild(vp);
    var side = make('div', 'demo-side');
    var stepno = make('div', 'demo-stepno'), cap = make('div', 'demo-cap'), todo = make('ol', 'demo-todo');
    cap.setAttribute('aria-live', 'polite');
    def.steps.forEach(function (s, k) { todo.appendChild(make('li', '', '<i>' + (k + 1) + '</i><span>' + s.check + '</span>')); });
    var controls = make('div', 'demo-controls',
      '<button type="button" data-act="back">◀ Back</button><button type="button" data-act="next">Next ▶</button>' +
      '<button type="button" data-act="auto" aria-pressed="false">Auto</button>' +
      '<button type="button" data-act="replay" aria-label="Replay from the start">↺</button>' +
      '<button type="button" data-act="slow" aria-pressed="false" aria-label="Half speed">½×</button>');
    side.appendChild(stepno); side.appendChild(cap); side.appendChild(todo); side.appendChild(controls);
    host.appendChild(bezel); host.appendChild(side);

    var screen, cursor, spot, idx = 0, token = 0, busy = false, spd = 1, auto = false, base = 1, cam = { z: 1, px: W / 2, py: H / 2 };
    var view = { tx: 0, ty: 0, s: 1 };
    var wait = function (ms) { return new Promise(function (r) { setTimeout(r, reduce ? 0 : ms * spd); }); };

    function camera(anim) {
      var s = base * cam.z, bw = vp.clientWidth, bh = vp.clientHeight;
      var tx = Math.min(0, Math.max(bw - W * s, bw / 2 - cam.px * s));
      var ty = Math.min(0, Math.max(bh - H * s, bh / 2 - cam.py * s));
      view = { tx: tx, ty: ty, s: s };
      screen.style.transition = anim && !reduce ? 'transform ' + CAM_MS * spd + 'ms ' + CAM_EASE : 'none';
      screen.style.transform = 'translate(' + tx + 'px,' + ty + 'px) scale(' + s + ')';
    }
    /* True when the point already sits well inside the current view, so the camera can stay still. */
    function inView(p) {
      var x = view.tx + p.x * view.s, y = view.ty + p.y * view.s, bw = vp.clientWidth, bh = vp.clientHeight;
      return x > bw * 0.2 && x < bw * 0.8 && y > bh * 0.2 && y < bh * 0.8;
    }
    /* One glide per step: zoom: false shows the step on the whole screen; otherwise a gentle zoom, capped. */
    function aim(step, p) {
      var z = step.zoom === false ? 1 : Math.min(step.zoom || ZOOM, MAX_ZOOM);
      if (cam.z === z && (z === 1 || inView(p))) return;
      cam = z === 1 ? { z: 1, px: W / 2, py: H / 2 } : { z: z, px: p.x, py: p.y };
      camera(true);
    }
    function fit() { base = vp.clientWidth / W || 1; if (screen) camera(false); }
    if (global.ResizeObserver) new ResizeObserver(fit).observe(vp);

    function ui(i) {
      stepno.textContent = 'STEP ' + (i + 1) + ' / ' + def.steps.length;
      cap.innerHTML = def.steps[i].cap;
      Array.prototype.forEach.call(todo.children, function (li, k) { li.className = k < i ? 'done' : k === i ? 'now' : ''; });
    }
    function point(step) {
      var t = step.target && screen.querySelector(step.target);
      if (!t) return null;
      var p = offset(t, screen), at = step.at || [0.5, 0.5];
      return { box: p, x: p.x + p.w * at[0], y: p.y + p.h * at[1] };
    }
    function place(x, y, anim) {
      cursor.style.transition = anim && !reduce ? 'left ' + CURSOR_MS * spd + 'ms ' + CAM_EASE + ', top ' + CURSOR_MS * spd + 'ms ' + CAM_EASE : 'none';
      cursor.style.left = x + 'px'; cursor.style.top = y + 'px';
    }
    function render(i) {
      var fresh = make('div', 'screen ' + (def.screenClass || ''), def.scene);
      spot = make('div', 'demo-spot'); cursor = make('div', 'demo-cursor', CURSOR);
      fresh.appendChild(spot); fresh.appendChild(cursor);
      if (screen) vp.replaceChild(fresh, screen); else vp.appendChild(fresh);
      screen = fresh;
      for (var k = 0; k <= i; k++) applyState(screen, def.steps[k].state);
      var start = def.start || [640, 400], last = null;
      for (var j = i; j >= 0 && !last; j--) {
        var s = def.steps[j];
        if (!s.target) continue;
        var el = screen.querySelector(s.target);
        if (!el || el.offsetParent === null || el.getClientRects().length === 0) continue;
        last = point(s);
      }
      place(last ? last.x : start[0], last ? last.y : start[1], false);
      cam = { z: 1, px: W / 2, py: H / 2 }; fit();
    }
    function jump(i) { token++; busy = false; idx = i; render(i); ui(i); }

    function play(i) {
      var my = ++token, step = def.steps[i];
      busy = true; idx = i; ui(i);
      if (reduce || !step.target) { render(i); busy = false; return Promise.resolve(); }
      var p = point(step);
      if (!p) { console.error('DL2Demo: missing target', step.target, 'in', def.id); render(i); busy = false; return Promise.resolve(); }
      aim(step, p);
      place(p.x, p.y, true);
      return wait(CAM_MS).then(function () {
        if (my !== token) return;
        Object.assign(spot.style, { left: p.box.x - 6 + 'px', top: p.box.y - 6 + 'px', width: p.box.w + 12 + 'px', height: p.box.h + 12 + 'px' });
        spot.classList.add('on');
        return wait(500);
      }).then(function () {
        if (my !== token) return;
        if (step.action === 'type' && step.text) {
          var t = screen.querySelector(step.target), chars = step.text.split(''), n = 0;
          return new Promise(function (done) {
            (function tick() {
              if (my !== token) return done();
              if (n >= chars.length) return done();
              if ('value' in t) t.value += chars[n++]; else t.textContent += chars[n++];
              setTimeout(tick, 55 * spd);
            })();
          });
        }
        if (step.action !== 'hover' && step.action !== 'none') {
          cursor.classList.add('press');
          var r = make('div', 'demo-ripple'); r.style.left = p.x + 'px'; r.style.top = p.y + 'px'; screen.appendChild(r);
          setTimeout(function () { r.remove(); cursor.classList.remove('press'); }, 700 * spd);
        }
        return wait(380);
      }).then(function () {
        if (my !== token) return;
        spot.classList.remove('on');
        applyState(screen, step.state);
        if (step.zoomOut) { cam = { z: 1, px: W / 2, py: H / 2 }; camera(true); }
        busy = false;
      });
    }

    var ctl = {
      index: function () { return idx; },
      next: function () {
        /* Mid-animation, Next finishes the current step on screen and is used up by that, even on
         * the last step, so a quick presenter always sees each result before moving on. */
        if (busy) { jump(idx); return true; }
        if (idx >= def.steps.length - 1) return false;
        play(idx + 1); return true;
      },
      back: function () { if (idx <= 0) return false; setAuto(false); jump(idx - 1); return true; },
      reset: function () { setAuto(false); jump(0); }
    };
    function setAuto(on) {
      auto = on;
      controls.querySelector('[data-act="auto"]').setAttribute('aria-pressed', String(on));
      if (!on) return;
      (function loop() {
        if (!auto) return;
        if (idx >= def.steps.length - 1) { setAuto(false); return; }
        Promise.resolve(play(idx + 1)).then(function () { if (auto) setTimeout(loop, 2200 * spd); });
      })();
    }
    controls.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b) return;
      var act = b.dataset.act;
      if (act === 'next') { setAuto(false); ctl.next(); }
      else if (act === 'back') ctl.back();
      else if (act === 'replay') ctl.reset();
      else if (act === 'auto') setAuto(!auto);
      else if (act === 'slow') { spd = spd === 1 ? 2 : 1; b.setAttribute('aria-pressed', String(spd === 2)); }
    });

    jump(0);
    controllers[def.id] = ctl;
    var slide = host.closest('.slide');
    if (slide && global.DL2Deck) global.DL2Deck.registerStepper(slide, ctl);
    return ctl;
  }

  function mountAll() { Array.prototype.forEach.call(document.querySelectorAll('[data-demo]'), mount); }
  global.DL2Demo = { define: define, mount: mount, get: function (id) { return controllers[id]; } };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mountAll);
  else setTimeout(mountAll, 0);
})(window);
