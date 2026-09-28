/* Week 1 Show demos: Windows 11 + Microsoft 365 recreations with fictional data.
 * Every scene is authored at 1280x720 inside .screen (see demo.js). Windows text uses div/span only:
 * the deck puts !important font sizes on p/li/td/th/h1/h2, and shared/text-size.js resizes
 * a/button/label/input, so none of those tags appear in a scene.
 *
 * Layout of this file:
 *   1. Icons (I.*)             inline SVG strings, flat colours, no gradient ids
 *   2. Shared chrome           taskbar(), caption(), win(), desktop()
 *   3. Settings kit            settingsNav(), card(), combo()
 *   4. Quick Settings kit      quickSettings()
 *   5. Word kit                wordWin(), wordRail(), printPage()
 *   6. Demos                   DL2Demo.define(...) — append new demos at the end of this section. */
(function () {
  'use strict';

  /* ============================== 1. Icons ============================== */
  function svg(size, vb, body, cls) {
    return '<svg' + (cls ? ' class="' + cls + '"' : '') + ' width="' + size + '" height="' + size + '" viewBox="' + vb + '" aria-hidden="true">' + body + '</svg>';
  }
  function line(d, w, color) {
    return '<path d="' + d + '" fill="none" stroke="' + (color || 'currentColor') + '" stroke-width="' + (w || 1.3) + '" stroke-linecap="round" stroke-linejoin="round"/>';
  }
  // A filled gear with a hole: `teeth` rectangular teeth between rIn and rOut.
  function gearPath(c, rOut, rIn, rHole, teeth) {
    var step = Math.PI * 2 / teeth, d = '';
    function pt(r, a) { return (c + r * Math.cos(a)).toFixed(2) + ' ' + (c + r * Math.sin(a)).toFixed(2); }
    for (var t = 0; t < teeth; t++) {
      var a = t * step - Math.PI / 2;
      d += (t ? 'L' : 'M') + pt(rIn, a) + 'L' + pt(rOut, a + step * 0.12) + 'L' + pt(rOut, a + step * 0.42) + 'L' + pt(rIn, a + step * 0.54) +
        'A' + rIn + ' ' + rIn + ' 0 0 1 ' + pt(rIn, a + step);
    }
    d += 'ZM' + (c - rHole) + ' ' + c + 'a' + rHole + ' ' + rHole + ' 0 1 0 ' + 2 * rHole + ' 0a' + rHole + ' ' + rHole + ' 0 1 0 ' + -2 * rHole + ' 0Z';
    return '<path fill-rule="evenodd" d="' + d + '"/>';
  }

  var SPEAKER = 'M2.5 7.5h3L10 4v12l-4.5-3.5h-3z';
  var I = {
    // taskbar apps (24px)
    start: svg(24, '0 0 24 24', '<rect x="2" y="2" width="9.6" height="9.6" rx="1.3" fill="#3ea3ff"/><rect x="12.4" y="2" width="9.6" height="9.6" rx="1.3" fill="#2690f4"/><rect x="2" y="12.4" width="9.6" height="9.6" rx="1.3" fill="#1b80e6"/><rect x="12.4" y="12.4" width="9.6" height="9.6" rx="1.3" fill="#0b6dd3"/>'),
    search: svg(22, '0 0 24 24', '<circle cx="10.5" cy="10.5" r="6.3" fill="none" stroke="#1a1a1a" stroke-width="1.9"/>' + line('M15.3 15.3L20.5 20.5', 2.1, '#1a1a1a')),
    explorer: svg(24, '0 0 24 24', '<path d="M2 6.5A1.8 1.8 0 0 1 3.8 4.7h5.3l2.1 2.1h9A1.8 1.8 0 0 1 22 8.6v9.9a1.8 1.8 0 0 1-1.8 1.8H3.8A1.8 1.8 0 0 1 2 18.5z" fill="#e9a52c"/><path d="M2 10.2A1.8 1.8 0 0 1 3.8 8.4h16.4A1.8 1.8 0 0 1 22 10.2v8.3a1.8 1.8 0 0 1-1.8 1.8H3.8A1.8 1.8 0 0 1 2 18.5z" fill="#ffcb4c"/><rect x="2" y="14.6" width="20" height="2.4" fill="#2a8ad8"/>'),
    edge: svg(24, '0 0 24 24', '<path d="M21.7 13.4C21.7 7.6 17.4 2.6 11.7 2.6 6.3 2.6 2.3 7 2.3 12.3c0 5.4 4.3 9.3 9.5 9.3 3.2 0 6-1.4 7.8-3.8-3.4 1.6-8.7.7-9.2-3.9-.3-2.5 1.6-4.4 4.1-4.4 2.8 0 4.7 1.7 4.7 3.9 0 .5-.1 1-.3 1.4 1.8.2 2.8-.5 2.8-1.4z" fill="#1b8ee3"/><path d="M10.4 13.9c.5 4.6 5.8 5.5 9.2 3.9-1.8 2.4-4.6 3.8-7.8 3.8-5.2 0-9.5-3.9-9.5-9.3 0-.5 0-.9.1-1.3 1.4-3.2 5.2-4.4 7.6-2.8-1.2 1.1-1.8 3.1-1.6 5.7z" fill="#35c46f"/>'),
    word: svg(24, '0 0 24 24', '<path d="M7.5 2.5h12.7a1.3 1.3 0 0 1 1.3 1.3V7.5h-14z" fill="#41a5ee"/><rect x="7.5" y="7.5" width="14" height="5" fill="#2b7cd3"/><rect x="7.5" y="12.5" width="14" height="4.5" fill="#185abd"/><path d="M7.5 17h14v3.2a1.3 1.3 0 0 1-1.3 1.3H8.8a1.3 1.3 0 0 1-1.3-1.3z" fill="#103f91"/><rect x="2.5" y="6.5" width="11" height="11" rx="1.3" fill="#185abd"/><path d="M4.6 9.2l1.3 5.6h1.1L8 11.2l1 3.6h1.1l1.3-5.6h-1l-.8 3.9-1-3.9h-1.2l-1 3.9-.8-3.9z" fill="#fff"/>'),
    outlook: svg(24, '0 0 24 24', '<rect x="7.5" y="3" width="14" height="17.5" rx="1.5" fill="#0a5fb8"/><path d="M7.5 10.5l7 4.6 7-4.6v8.5a1.5 1.5 0 0 1-1.5 1.5H9a1.5 1.5 0 0 1-1.5-1.5z" fill="#28a8ea"/><rect x="2.5" y="6.5" width="11" height="11" rx="1.3" fill="#0f6cbd"/><ellipse cx="8" cy="12" rx="2.5" ry="3" fill="none" stroke="#fff" stroke-width="1.5"/>'),
    settings: svg(24, '0 0 24 24', '<g fill="#5b5b5b">' + gearPath(12, 10.2, 7.6, 3.4, 8) + '</g>'),
    // tray (16px)
    chevUp: svg(16, '0 0 16 16', line('M4 10l4-4 4 4', 1.2)),
    wifi: svg(16, '0 0 16 16', line('M1.3 6.1a9.8 9.8 0 0 1 13.4 0M3.6 8.6a6.5 6.5 0 0 1 8.8 0M5.9 11.1a3.3 3.3 0 0 1 4.2 0', 1.25) + '<circle cx="8" cy="13.4" r="1.1" fill="currentColor"/>'),
    speaker: svg(16, '0 0 20 20', line(SPEAKER, 1.4) + line('M13 7.6a3.4 3.4 0 0 1 0 4.8M15.4 5.3a6.8 6.8 0 0 1 0 9.4', 1.4)),
    battery: svg(16, '0 0 16 16', '<rect x="1" y="4.6" width="12.3" height="6.8" rx="1.6" fill="none" stroke="currentColor" stroke-width="1.1"/><rect x="2.6" y="6.2" width="7.6" height="3.6" rx=".6" fill="currentColor"/>' + line('M14.6 6.8v2.4', 1.3)),
    bell: svg(16, '0 0 16 16', line('M8 2.3a3.7 3.7 0 0 0-3.7 3.7v2.7L3 11.2h10l-1.3-2.5V6A3.7 3.7 0 0 0 8 2.3zM6.4 12.9a1.7 1.7 0 0 0 3.2 0', 1.1)),
    // Quick Settings (20px)
    wifi20: svg(20, '0 0 20 20', line('M1.8 7.6a11.8 11.8 0 0 1 16.4 0M4.6 10.6a7.9 7.9 0 0 1 10.8 0M7.3 13.6a4 4 0 0 1 5.4 0', 1.5) + '<circle cx="10" cy="16.4" r="1.3" fill="currentColor"/>'),
    bluetooth: svg(20, '0 0 20 20', line('M5.8 6.3l8 7.2L10 17V3l3.8 3.5-8 7.2', 1.5)),
    airplane: svg(20, '0 0 20 20', line('M8.6 11.2L6 17.5h1.6l4.4-6.3h4.3a1.3 1.3 0 0 0 0-2.4H12L7.6 2.5H6l2.6 6.3H4.9L3.4 7H2.3l.9 3-.9 3h1.1l1.5-1.8z', 1.3)),
    leaf: svg(20, '0 0 20 20', line('M4.2 16.3C3.4 8.7 8.6 4 16.4 3.6c.5 7.9-4.3 12.9-11.6 12.3M4.2 16.3l6.3-6.3', 1.4)),
    access: svg(20, '0 0 20 20', '<circle cx="10" cy="4.3" r="1.7" fill="currentColor"/>' + line('M3.5 7.3l6.5 1.6 6.5-1.6M10 8.9v3.6l-3 5M10 12.5l3 5', 1.5)),
    moon: svg(20, '0 0 20 20', line('M11.6 3.2a7 7 0 1 0 5.2 10.4 5.9 5.9 0 0 1-5.2-10.4z', 1.4)),
    sun: svg(20, '0 0 20 20', '<circle cx="10" cy="10" r="3.4" fill="none" stroke="currentColor" stroke-width="1.4"/>' + line('M10 1.8v2M10 16.2v2M1.8 10h2M16.2 10h2M4.2 4.2l1.4 1.4M14.4 14.4l1.4 1.4M4.2 15.8l1.4-1.4M14.4 5.6l1.4-1.4', 1.4)),
    speaker20: svg(20, '0 0 20 20', line(SPEAKER, 1.4) + line('M13 7.6a3.4 3.4 0 0 1 0 4.8M15.4 5.3a6.8 6.8 0 0 1 0 9.4', 1.4)),
    headphones: svg(20, '0 0 20 20', line('M3.4 12.2v-1.7a6.6 6.6 0 0 1 13.2 0v1.7M3.4 12.2H6v5H4.7a1.3 1.3 0 0 1-1.3-1.3zM16.6 12.2H14v5h1.3a1.3 1.3 0 0 0 1.3-1.3z', 1.4)),
    pencil: svg(18, '0 0 20 20', line('M12.8 3.6l3.6 3.6-9.5 9.5H3.3v-3.6zM10.8 5.6l3.6 3.6', 1.3)),
    gear18: svg(18, '0 0 24 24', '<g fill="currentColor">' + gearPath(12, 10, 7.4, 3.3, 8) + '</g>'),
    chevR: svg(16, '0 0 16 16', line('M6 3.5L10.5 8 6 12.5', 1.3)),
    chevL: svg(16, '0 0 16 16', line('M10 3.5L5.5 8l4.5 4.5', 1.3)),
    chevD: svg(12, '0 0 12 12', line('M2.5 4.5L6 8l3.5-3.5', 1.1)),
    // title bars
    gear16: svg(16, '0 0 24 24', '<g fill="#5b5b5b">' + gearPath(12, 10.2, 7.6, 3.4, 8) + '</g>')
  };

  /* ============================ 2. Shared chrome ============================ */
  /* taskbar(apps, open): centered pinned apps (keys of I), `.open` under the running one,
   * then the system tray: overflow ^, the network/volume/battery button (#tray-sound = speaker),
   * the clock and the notification bell. */
  function taskbar(apps, open) {
    return '<div class="w11-taskbar">' + apps.map(function (a) {
      return '<span class="w11-tbi' + (a === open ? ' open' : '') + '" data-app="' + a + '">' + I[a] + '</span>';
    }).join('') +
      '<span class="w11-tray"><span class="w11-tray-btn">' + I.chevUp + '</span>' +
      '<span class="w11-tray-btn w11-tray-icons"><span>' + I.wifi + '</span><span id="tray-sound">' + I.speaker + '</span><span>' + I.battery + '</span></span>' +
      '<span class="w11-tray-btn w11-clock"><span>4:52 PM</span><span>9/28/2026</span></span>' +
      '<span class="w11-tray-btn w11-bell">' + I.bell + '</span></span></div>';
  }
  /* Caption buttons (minimize, maximize/restore, close) as crisp 10px strokes. */
  function caption(maximized, cls) {
    var min = svg(10, '0 0 10 10', '<path d="M0 5.5h10" stroke="currentColor" stroke-width="1"/>');
    var max = maximized
      ? svg(10, '0 0 10 10', '<path d="M2.5 2.5V1.2a.7.7 0 0 1 .7-.7h5.6a.7.7 0 0 1 .7.7v5.6a.7.7 0 0 1-.7.7H7.5" fill="none" stroke="currentColor" stroke-width="1"/><rect x=".5" y="2.5" width="7" height="7" rx=".7" fill="none" stroke="currentColor" stroke-width="1"/>')
      : svg(10, '0 0 10 10', '<rect x=".5" y=".5" width="9" height="9" rx="1" fill="none" stroke="currentColor" stroke-width="1"/>');
    var close = svg(10, '0 0 10 10', '<path d="M.5.5l9 9M9.5.5l-9 9" stroke="currentColor" stroke-width="1"/>');
    return '<span class="w11-ctl' + (cls ? ' ' + cls : '') + '"><span>' + min + '</span><span>' + max + '</span><span>' + close + '</span></span>';
  }
  /* win(title, icon, body, cls): a floating Windows 11 app window (Mica title bar). */
  function win(title, icon, body, cls) {
    return '<div class="w11-win ' + (cls || '') + '"><div class="w11-title">' + I[icon] + '<span>' + title + '</span>' + caption(false) + '</div>' + body + '</div>';
  }
  /* desktop(icons): wallpaper plus desktop shortcuts [{icon, label}]. */
  var DESK = {
    bin: svg(44, '0 0 44 44', '<path d="M9 12h26l-2.4 26.2a2 2 0 0 1-2 1.8H13.4a2 2 0 0 1-2-1.8z" fill="#dfeefe" stroke="#6c9fd6" stroke-width="1.2"/><path d="M7 12h30" stroke="#6c9fd6" stroke-width="2" stroke-linecap="round"/><path d="M17 8.5h10" stroke="#6c9fd6" stroke-width="2" stroke-linecap="round"/><path d="M17 18l1 16M22 18v16M27 18l-1 16" stroke="#9cc0e8" stroke-width="1.4"/>'),
    folder: svg(44, '0 0 24 24', '<path d="M2 6.5A1.8 1.8 0 0 1 3.8 4.7h5.3l2.1 2.1h9A1.8 1.8 0 0 1 22 8.6v9.9a1.8 1.8 0 0 1-1.8 1.8H3.8A1.8 1.8 0 0 1 2 18.5z" fill="#e9a52c"/><path d="M2 10.2A1.8 1.8 0 0 1 3.8 8.4h16.4A1.8 1.8 0 0 1 22 10.2v8.3a1.8 1.8 0 0 1-1.8 1.8H3.8A1.8 1.8 0 0 1 2 18.5z" fill="#ffcb4c"/>')
  };
  function desktop(icons) {
    return '<div class="w11-wall"></div><div class="w11-desk">' + (icons || []).map(function (d) {
      return '<span class="w11-dicon">' + DESK[d.icon] + '<span>' + d.label + '</span></span>';
    }).join('') + '</div>';
  }

  /* ============================ 3. Settings kit ============================ */
  function ci(body) { return svg(24, '0 0 24 24', body, 'ci'); }
  var NAV = [
    ['Home', '<path d="M3 11l9-7 9 7v9h-6v-6H9v6H3z" fill="#4a88d8"/>'],
    ['System', '<rect x="3" y="4" width="18" height="12" rx="2" fill="#0f6cbd"/><path d="M9 20h6M12 16v4" stroke="#0f6cbd" stroke-width="2"/>'],
    ['Bluetooth &amp; devices', '<rect x="4" y="6" width="10" height="12" rx="2" fill="#3a7bd5"/><rect x="15" y="9" width="5" height="9" rx="1.5" fill="#6aa5ef"/>'],
    ['Network &amp; internet', '<path d="M2 9a15 15 0 0 1 20 0M5.5 12.5a10 10 0 0 1 13 0M9 16a5 5 0 0 1 6 0" fill="none" stroke="#2b67c6" stroke-width="2.2" stroke-linecap="round"/><circle cx="12" cy="19" r="1.6" fill="#2b67c6"/>'],
    ['Personalization', '<path d="M14 4l6 6-8 8H6v-6z" fill="#e8883a"/>'],
    ['Apps', '<rect x="3" y="3" width="8" height="8" rx="1.5" fill="#5b6b82"/><rect x="13" y="3" width="8" height="8" rx="1.5" fill="#5b6b82"/><rect x="3" y="13" width="8" height="8" rx="1.5" fill="#5b6b82"/><rect x="13" y="13" width="8" height="8" rx="1.5" fill="#5b6b82"/>'],
    ['Accounts', '<circle cx="12" cy="8" r="4" fill="#2e9e5b"/><path d="M4 21c1-5 15-5 16 0" fill="#2e9e5b"/>'],
    ['Time &amp; language', '<circle cx="12" cy="12" r="9" fill="none" stroke="#3a7bd5" stroke-width="2"/><path d="M12 7v5l3 2" stroke="#3a7bd5" stroke-width="2" fill="none"/>'],
    ['Gaming', '<path d="M7 8h10a4 4 0 0 1 3.9 4.9l-.8 3.4a2 2 0 0 1-3.4.9L15 15.5H9l-1.7 1.7a2 2 0 0 1-3.4-.9l-.8-3.4A4 4 0 0 1 7 8z" fill="#6b7890"/><path d="M8 10.5v3M6.5 12h3" stroke="#fff" stroke-width="1.4" stroke-linecap="round"/><circle cx="15.5" cy="11" r="1" fill="#fff"/><circle cx="17" cy="13" r="1" fill="#fff"/>'],
    ['Accessibility', '<circle cx="12" cy="12" r="9.5" fill="#1f6fd1"/><circle cx="12" cy="7.5" r="1.6" fill="#fff"/><path d="M7.5 10h9M12 10v4l-2.5 4.5M12 14l2.5 4.5" stroke="#fff" stroke-width="1.7" stroke-linecap="round" fill="none"/>'],
    ['Privacy &amp; security', '<path d="M12 2l8 3v6c0 5-3.5 9-8 11-4.5-2-8-6-8-11V5z" fill="#6b7890"/>'],
    ['Windows Update', '<path d="M20 12a8 8 0 1 1-2.3-5.6M20 4v5h-5" fill="none" stroke="#0f6cbd" stroke-width="2.2" stroke-linecap="round"/>']
  ];
  function settingsNav(sel) {
    return '<div class="w11-nav"><div class="w11-acct"><div class="w11-avatar">VL</div><div><b>Veteran Learner</b><small>Local account</small></div></div>' +
      '<div class="w11-search"><span>Find a setting</span>' + svg(14, '0 0 24 24', '<circle cx="10" cy="10" r="6" fill="none" stroke="#444" stroke-width="2"/><path d="M15 15l5 5" stroke="#444" stroke-width="2"/>') + '</div>' +
      NAV.map(function (n) { return '<div class="w11-navi' + (n[0] === sel ? ' sel' : '') + '">' + svg(24, '0 0 24 24', n[1]) + '<span>' + n[0] + '</span></div>'; }).join('') + '</div>';
  }
  /* card({id, icon, title, sub, right, chev}): one Settings row. */
  function card(o) {
    return '<div class="w11-card"' + (o.id ? ' id="' + o.id + '"' : '') + '>' + ci(o.icon) +
      '<div class="ct"><b>' + o.title + '</b>' + (o.sub ? '<small>' + o.sub + '</small>' : '') + '</div>' +
      (o.right || '') + (o.chev ? '<span class="chev">' + I.chevR + '</span>' : '') + '</div>';
  }
  function combo(id, valId, value, flyout) {
    return '<div class="w11-combo"' + (id ? ' id="' + id + '"' : '') + '><span' + (valId ? ' id="' + valId + '"' : '') + '>' + value + '</span>' + I.chevD + (flyout || '') + '</div>';
  }
  var S = '#1a1a1a';
  var ICON = {
    display: '<rect x="3" y="4" width="18" height="12" rx="2" fill="none" stroke="' + S + '" stroke-width="1.6"/><path d="M9 20h6M12 16v4" stroke="' + S + '" stroke-width="1.6"/>',
    sound: '<path d="M4 9h4l5-4v14l-5-4H4z" fill="none" stroke="' + S + '" stroke-width="1.6"/><path d="M16 9a4 4 0 0 1 0 6M18.5 6.5a8 8 0 0 1 0 11" fill="none" stroke="' + S + '" stroke-width="1.6"/>',
    notify: '<path d="M6 16V11a6 6 0 0 1 12 0v5l2 2H4z M10 20h4" fill="none" stroke="' + S + '" stroke-width="1.6"/>',
    focus: '<circle cx="12" cy="12" r="8" fill="none" stroke="' + S + '" stroke-width="1.6"/><circle cx="12" cy="12" r="3" fill="none" stroke="' + S + '" stroke-width="1.6"/>',
    power: '<path d="M12 3v8M7 6.5a7 7 0 1 0 10 0" fill="none" stroke="' + S + '" stroke-width="1.6" stroke-linecap="round"/>',
    storage: '<rect x="4" y="5" width="16" height="6" rx="1.5" fill="none" stroke="' + S + '" stroke-width="1.6"/><rect x="4" y="13" width="16" height="6" rx="1.5" fill="none" stroke="' + S + '" stroke-width="1.6"/>',
    bright: '<circle cx="12" cy="12" r="4" fill="none" stroke="' + S + '" stroke-width="1.6"/><path d="M12 2.5v2.5M12 19v2.5M2.5 12H5M19 12h2.5M5.3 5.3l1.8 1.8M16.9 16.9l1.8 1.8M5.3 18.7l1.8-1.8M16.9 7.1l1.8-1.8" stroke="' + S + '" stroke-width="1.6" stroke-linecap="round"/>',
    night: '<path d="M12 4a8 8 0 1 0 8 8 6 6 0 0 1-8-8z" fill="none" stroke="' + S + '" stroke-width="1.6"/>',
    scale: '<rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="' + S + '" stroke-width="1.6"/><path d="M8 15l4-6 4 6" fill="none" stroke="' + S + '" stroke-width="1.6"/>',
    res: '<rect x="3" y="5" width="18" height="14" rx="2" fill="none" stroke="' + S + '" stroke-width="1.6"/><path d="M7 9h4M7 9v4M17 15h-4M17 15v-4" stroke="' + S + '" stroke-width="1.6"/>',
    orient: '<rect x="5" y="3" width="14" height="18" rx="2" fill="none" stroke="' + S + '" stroke-width="1.6"/><path d="M9 18h6" stroke="' + S + '" stroke-width="1.6"/>'
  };

  var SYSTEM_PAGE = '<div class="w11-page" data-page="system"><div class="w11-h1">System</div>' +
    card({ id: 'card-display', icon: ICON.display, title: 'Display', sub: 'Monitors, brightness, night light, display profile', chev: true }) +
    card({ icon: ICON.sound, title: 'Sound', sub: 'Volume levels, output, input, sound devices', chev: true }) +
    card({ icon: ICON.notify, title: 'Notifications', sub: 'Alerts from apps and system, do not disturb', chev: true }) +
    card({ icon: ICON.focus, title: 'Focus', sub: 'Reduce distractions', chev: true }) +
    card({ icon: ICON.power, title: 'Power &amp; battery', sub: 'Sleep, battery usage, energy saver', chev: true }) +
    card({ icon: ICON.storage, title: 'Storage', sub: 'Storage space, drives, configuration rules', chev: true }) + '</div>';

  var SCALE_FLYOUT = '<div class="w11-flyout"><div class="w11-opt sel">100% (Recommended)</div><div class="w11-opt" id="opt-125">125%</div><div class="w11-opt">150%</div><div class="w11-opt">175%</div></div>';
  var DISPLAY_PAGE = '<div class="w11-page" data-page="display"><div class="w11-h1"><span class="parent">System</span><span class="sep">›</span><span>Display</span></div>' +
    '<div class="w11-sect">Brightness &amp; color</div>' +
    card({ icon: ICON.bright, title: 'Brightness', sub: 'Adjust the brightness of the built-in display', right: '<span class="w11-slider w11-card-slider" style="--v:70%"><i></i></span>', chev: true }) +
    card({ icon: ICON.night, title: 'Night light', sub: 'Use warmer colors to help block blue light', right: '<div class="w11-toggle">Off <i></i></div>', chev: true }) +
    '<div class="w11-sect">Scale &amp; layout</div>' +
    card({ icon: ICON.scale, title: 'Scale', sub: 'Change the size of text, apps, and other items', right: combo('scale-dd', 'scale-val', '100% (Recommended)', SCALE_FLYOUT), chev: true }) +
    card({ icon: ICON.res, title: 'Display resolution', sub: 'Adjust the resolution to fit your connected display', right: combo('', '', '1920 × 1080 (Recommended)') }) +
    card({ icon: ICON.orient, title: 'Display orientation', right: combo('', '', 'Landscape') }) + '</div>';

  /* ========================== 4. Quick Settings kit ========================== */
  function qsTile(icon, label, on, split) {
    return '<span class="w11-qs-cell"><span class="w11-qs-tile' + (on ? ' on' : '') + (split ? ' split' : '') + '"><span class="w11-qs-main-ico">' + I[icon] + '</span>' +
      (split ? '<span class="w11-qs-split">' + I.chevR + '</span>' : '') + '</span><span class="w11-qs-lab">' + label + '</span></span>';
  }
  function qsDevice(id, icon, name) {
    return '<div class="w11-qs-dev" id="' + id + '"><span class="w11-qs-ico">' + I[icon] + '</span><span class="w11-qs-name">' + name + '</span><span class="tick">✓</span></div>';
  }
  function quickSettings() {
    var main = '<div class="w11-qs-main"><div class="w11-qs-top"><div class="w11-qs-tiles">' +
      qsTile('wifi20', 'Lab-WiFi', true, true) + qsTile('bluetooth', 'Bluetooth', false, true) + qsTile('airplane', 'Airplane mode') +
      qsTile('leaf', 'Energy saver') + qsTile('access', 'Accessibility', false, true) + qsTile('moon', 'Night light') +
      '</div><span class="w11-qs-pager"><i class="on"></i><i></i></span></div>' +
      '<div class="w11-qs-row"><span class="w11-qs-ico">' + I.sun + '</span><span class="w11-slider" style="--v:70%"><i></i></span><span class="w11-qs-more w11-qs-blank"></span></div>' +
      '<div class="w11-qs-row"><span class="w11-qs-ico">' + I.speaker20 + '</span><span class="w11-slider" style="--v:40%"><i></i></span>' +
      '<span class="w11-qs-more" id="qs-output" role="button" aria-label="Select a sound output" title="Select a sound output">' + I.chevR + '</span></div>' +
      '<div class="w11-qs-foot"><span class="w11-qs-batt">' + I.battery + '<span>82%</span></span><span class="w11-qs-fbtn">' + I.pencil + '</span><span class="w11-qs-fbtn">' + I.gear18 + '</span></div></div>';
    var out = '<div class="w11-qs-out"><div class="w11-qs-head"><span class="w11-qs-back">' + I.chevL + '</span><span>Sound output</span></div>' +
      '<div class="w11-qs-list">' + qsDevice('out-speakers', 'speaker20', 'Speakers (Realtek(R) Audio)') + qsDevice('out-headphones', 'headphones', 'Headphones (USB Audio Device)') + '</div>' +
      '<div class="w11-qs-div"></div><div class="w11-qs-label">Volume mixer</div>' +
      '<div class="w11-qs-row w11-qs-mix"><span class="w11-qs-ico">' + I.speaker20 + '</span><span class="w11-qs-name">System sounds</span><span class="w11-slider" style="--v:100%"><i></i></span></div>' +
      '<div class="w11-qs-foot"><span class="w11-qs-link">More volume settings</span></div></div>';
    return '<div class="w11-qs">' + main + out + '</div>';
  }

  /* ============================== 5. Word kit ============================== */
  var W = '#444';
  var WI = {
    save: svg(16, '0 0 16 16', line('M2.5 2.5h8.5l2.5 2.5v8.5h-11zM5 2.5v3.5h5.5v-3.5M4.5 13.5v-4.5h7v4.5', 1.1)),
    undo: svg(16, '0 0 16 16', line('M4 6.5h6.2a3.3 3.3 0 0 1 0 6.6H6.5M6.5 3.8L3.8 6.5l2.7 2.7', 1.2)),
    redo: svg(16, '0 0 16 16', line('M12 6.5H5.8a3.3 3.3 0 0 0 0 6.6h3.7M9.5 3.8l2.7 2.7-2.7 2.7', 1.2)),
    search: svg(14, '0 0 16 16', '<circle cx="6.8" cy="6.8" r="4.6" fill="none" stroke="currentColor" stroke-width="1.3"/>' + line('M10.3 10.3l3.8 3.8', 1.4)),
    back: svg(30, '0 0 30 30', '<circle cx="15" cy="15" r="13.5" fill="none" stroke="#fff" stroke-width="1.2"/>' + line('M20 15H10m4-4l-4 4 4 4', 1.4, '#fff')),
    home: svg(18, '0 0 20 20', line('M3 9.5L10 3.5l7 6M5 8v8.5h4v-4.5h2v4.5h4V8', 1.2, '#fff')),
    newdoc: svg(18, '0 0 20 20', line('M5 2.5h6.5l3.5 3.5v11.5H5zM11.5 2.5V6H15M10 9v6M7 12h6', 1.2, '#fff')),
    open: svg(18, '0 0 20 20', line('M2.5 5.5a1 1 0 0 1 1-1h4l1.5 1.5h7.5a1 1 0 0 1 1 1v9a1 1 0 0 1-1 1h-13a1 1 0 0 1-1-1z', 1.2, '#fff')),
    printer: svg(34, '0 0 34 34', line('M10 12V4.5h14V12', 1.4, W) + '<rect x="4" y="12" width="26" height="12.5" rx="2.2" fill="#fff" stroke="' + W + '" stroke-width="1.4"/>' +
      '<rect x="10" y="19.5" width="14" height="10" fill="#fff" stroke="' + W + '" stroke-width="1.4"/>' + line('M13 23h8M13 26h6', 1.2, W) + '<circle cx="25.5" cy="16" r="1.2" fill="#185abd"/>'),
    printer20: svg(22, '0 0 22 22', line('M6.5 7.5v-4h9v4', 1.2, W) + '<rect x="2.5" y="7.5" width="17" height="8.5" rx="1.5" fill="#fff" stroke="' + W + '" stroke-width="1.2"/><rect x="6.5" y="12.5" width="9" height="6.5" fill="#fff" stroke="' + W + '" stroke-width="1.2"/>' +
      '<circle cx="17" cy="17.5" r="3.6" fill="#107c10"/>' + line('M15.4 17.6l1.1 1.1 2-2.1', 1.1, '#fff')),
    info: svg(14, '0 0 16 16', '<circle cx="8" cy="8" r="6.6" fill="none" stroke="#616161" stroke-width="1.1"/><circle cx="8" cy="5" r=".85" fill="#616161"/>' + line('M8 7.2v4.2', 1.2, '#616161')),
    up: svg(8, '0 0 10 10', line('M2 6.5L5 3.5l3 3', 1.2, W)),
    down: svg(8, '0 0 10 10', line('M2 3.5L5 6.5l3-3', 1.2, W)),
    prev: svg(12, '0 0 12 12', '<path d="M8 2L3.5 6 8 10z" fill="currentColor"/>'),
    next: svg(12, '0 0 12 12', '<path d="M4 2l4.5 4L4 10z" fill="currentColor"/>'),
    fit: svg(16, '0 0 16 16', '<rect x="3" y="2" width="10" height="12" rx="1" fill="none" stroke="currentColor" stroke-width="1.1"/>' + line('M1 5V1h4M15 5V1h-4M1 11v4h4M15 11v4h-4', 1.1))
  };
  // Page glyphs for the Print settings drop-downs (28px); kind: all|oneside|collated|portrait|letter|margins|sheet
  function pageGlyph(kind) {
    var p = function (x, y, w, h) { return '<rect x="' + x + '" y="' + y + '" width="' + w + '" height="' + h + '" rx="1" fill="#fff" stroke="#6b6b6b" stroke-width="1"/>'; };
    var ln = function (x, y, w) { return '<path d="M' + x + ' ' + y + 'h' + w + '" stroke="#a0a0a0" stroke-width="1"/>'; };
    var body = {
      all: p(9, 3, 15, 19) + p(5, 7, 15, 19) + ln(8, 12, 9) + ln(8, 15, 9) + ln(8, 18, 6),
      oneside: p(7, 4, 15, 20) + ln(10, 9, 9) + ln(10, 12, 9) + ln(10, 15, 9) + ln(10, 18, 6),
      collated: p(3, 6, 10, 13) + p(9, 9, 10, 13) + p(15, 12, 10, 13) + '<text x="18.3" y="21.6" font-size="6" font-family="Segoe UI, sans-serif" fill="#444">3</text>',
      portrait: p(8, 3, 13, 20) + ln(11, 8, 7) + ln(11, 11, 7) + ln(11, 14, 7),
      letter: p(8, 3, 13, 20) + '<path d="M5 3v20M3.8 4.2L5 3l1.2 1.2M3.8 21.8L5 23l1.2-1.2" fill="none" stroke="#185abd" stroke-width=".9"/>',
      margins: p(6, 3, 17, 22) + '<rect x="9.5" y="6.5" width="10" height="15" fill="none" stroke="#185abd" stroke-width=".9" stroke-dasharray="1.6 1.2"/>',
      sheet: p(6, 3, 17, 22) + p(9.5, 6.5, 10, 15)
    }[kind];
    return svg(28, '0 0 28 28', body, 'wd-dd-ico');
  }
  /* Margin preset glyph for the margins menu: page 30x38 with the text block inset by (x, y) */
  function marginGlyph(x, y, mirrored) {
    return svg(34, '0 0 34 42', '<rect x="2" y="2" width="30" height="38" rx="1" fill="#fff" stroke="#8a8a8a" stroke-width="1"/>' +
      '<rect x="' + (2 + x) + '" y="' + (2 + y) + '" width="' + (30 - 2 * x - (mirrored ? 2 : 0)) + '" height="' + (38 - 2 * y) + '" fill="#e8eef9" stroke="#185abd" stroke-width=".8" stroke-dasharray="1.6 1.2"/>', 'wd-mi-ico');
  }

  /* wordWin(file, body): a maximized Microsoft 365 Word window with the blue title bar. */
  function wordWin(file, body) {
    return '<div class="wd-win"><div class="wd-title">' +
      '<span class="wd-qat"><span class="wd-autosave">AutoSave <span class="wd-sw"><i></i>Off</span></span><span class="wd-qi">' + WI.save + '</span><span class="wd-qi">' + WI.undo + '</span><span class="wd-qi wd-dim">' + WI.redo + '</span><span class="wd-qi">' + I.chevD + '</span></span>' +
      '<span class="wd-doc">' + file + ' - Word</span>' +
      '<span class="wd-search">' + WI.search + '<span>Search</span></span>' +
      '<span class="wd-user"><span>Veteran Learner</span><span class="wd-av">VL</span></span>' + caption(true, 'wd-ctl') +
      '</div>' + body + '</div>';
  }
  /* wordRail(): the File backstage rail. CSS highlights [data-rail="print"] on data-page="print" and
   * [data-rail="account"] on data-page="account", so the same rail serves every backstage page. */
  function wordRail() {
    var item = function (key, label, icon) { return '<div class="wd-ri" data-rail="' + key + '">' + (icon || '') + '<span>' + label + '</span></div>'; };
    return '<div class="wd-rail"><div class="wd-rback">' + WI.back + '</div>' +
      item('home', 'Home', WI.home) + item('new', 'New', WI.newdoc) + item('open', 'Open', WI.open) + '<div class="wd-rdiv"></div>' +
      item('info', 'Info') + item('save', 'Save') + item('saveas', 'Save As') + item('print', 'Print') + item('share', 'Share') + item('export', 'Export') + item('close', 'Close') +
      '<div class="wd-rfoot">' + item('account', 'Account') + item('feedback', 'Feedback') + item('options', 'Options') + '</div></div>';
  }
  /* dd(icon, title, sub): one Print ▸ Settings drop-down (page glyph, two lines, chevron). */
  function dd(icon, title, sub) {
    return '<div class="wd-dd">' + pageGlyph(icon) + '<span class="wd-dd-t"><b>' + title + '</b>' + (sub ? '<small>' + sub + '</small>' : '') + '</span>' + I.chevD + '</div>';
  }
  var MARGINS = [
    ['m-normal', 'Normal', ['1"', '1"', '1"', '1"'], 11, 9],
    ['m-narrow', 'Narrow', ['0.5"', '0.5"', '0.5"', '0.5"'], 5, 5],
    ['m-moderate', 'Moderate', ['1"', '1"', '0.75"', '0.75"'], 8, 9],
    ['m-wide', 'Wide', ['1"', '1"', '2"', '2"'], 13, 9],
    ['m-mirrored', 'Mirrored', ['1"', '1"', '1.25"', '1"'], 11, 9]
  ];
  function marginsMenu() {
    return '<div class="w11-flyout wd-menu">' + MARGINS.map(function (m) {
      var v = m[2], mir = m[1] === 'Mirrored';
      return '<div class="wd-mi" id="' + m[0] + '">' + marginGlyph(m[3], m[4], mir) + '<span class="wd-mi-t"><b>' + m[1] + '</b>' +
        '<span class="wd-mi-g"><span>Top:</span><span>' + v[0] + '</span><span>Bottom:</span><span>' + v[1] + '</span>' +
        '<span>' + (mir ? 'Inside:' : 'Left:') + '</span><span>' + v[2] + '</span><span>' + (mir ? 'Outside:' : 'Right:') + '</span><span>' + v[3] + '</span></span></span></div>';
    }).join('') + '<div class="wd-mi-custom">Custom Margins...</div></div>';
  }
  var FLYER_LINES = [
    'Free supper for veterans and families',
    'Roast chicken, green beans, potatoes',
    'Apple pie, coffee and sweet tea',
    'Doors open at 5:00 PM',
    'Bring a friend or a neighbor',
    'Rides: sign up at the front desk',
    'Tell a volunteer about food allergies',
    'Hosted by the Community Skills Desk'
  ];
  var SPILL = 'Questions? Call (555) 010-0148';
  /* The flyer as Word previews it. With Normal margins the last line (.pv-spill) moves to page 2. */
  function flyerPage() {
    var art = svg(110, '0 0 110 60', '<circle cx="55" cy="30" r="22" fill="#fff" stroke="#c9a227" stroke-width="3"/><circle cx="55" cy="30" r="14" fill="none" stroke="#c9a227" stroke-width="1.5"/>' +
      '<path d="M20 12v13M16 12v8a4 4 0 0 0 8 0v-8M20 25v24" stroke="#fff" stroke-width="2.4" fill="none" stroke-linecap="round"/>' +
      '<path d="M92 49V12c-5 2.5-6.5 9-6.5 16H92" stroke="#fff" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>');
    return '<div class="pv-page pv-page1"><div class="pv-in"><div class="pv-banner">' + art + '</div><div class="pv-title">Community Supper</div>' +
      '<div class="pv-date">Thursday, October 8 · 5:30 PM · Grace Fellowship Hall</div><div class="pv-rule"></div>' +
      FLYER_LINES.map(function (t) { return '<div class="pv-line">' + t + '</div>'; }).join('') +
      '<div class="pv-line pv-spill">' + SPILL + '</div></div></div>';
  }
  function printPage() {
    var col = '<div class="wd-pcol"><div class="wd-h">Print</div>' +
      '<div class="wd-prow"><div class="wd-printbtn" id="print-btn">' + WI.printer + '<span>Print</span></div>' +
      '<div class="wd-copies"><span>Copies:</span><span class="wd-spin"><span>1</span><span class="wd-arrows">' + WI.up + WI.down + '</span></span></div></div>' +
      '<div class="wd-sub">Printer ' + WI.info + '</div>' +
      '<div class="wd-dd wd-printer">' + WI.printer20 + '<span class="wd-dd-t"><b>Lab Printer (HP LaserJet)</b><small>Ready</small></span>' + I.chevD + '</div>' +
      '<div class="wd-link wd-right">Printer Properties</div>' +
      '<div class="wd-sub">Settings</div>' +
      dd('all', 'Print All Pages', 'The whole thing') +
      '<div class="wd-pages"><span>Pages:</span><span class="wd-input"></span>' + WI.info + '</div>' +
      dd('oneside', 'Print One Sided', 'Only print on one side of the page') +
      dd('collated', 'Collated', '1,2,3 &nbsp; 1,2,3 &nbsp; 1,2,3') +
      dd('portrait', 'Portrait Orientation') +
      dd('letter', 'Letter', '8.5" x 11"') +
      '<div class="wd-dd" id="margins-dd">' + pageGlyph('margins') + '<span class="wd-dd-t"><b id="margins-val">Normal Margins</b>' +
      '<small class="wd-when-normal">Top: 1" Bottom: 1" Left: 1" Right: 1"</small><small class="wd-when-narrow">Top: 0.5" Bottom: 0.5" Left: 0.5" Right: 0.5"</small></span>' + I.chevD + marginsMenu() + '</div>' +
      dd('sheet', '1 Page Per Sheet') +
      '<div class="wd-link wd-right">Page Setup</div></div>';
    var preview = '<div class="wd-preview"><div class="wd-pages-view">' + flyerPage() +
      '<div class="pv-page pv-page2"><div class="pv-in"><div class="pv-line">' + SPILL + '</div></div></div></div>' +
      '<div class="wd-pager"><span class="wd-pg-btn">' + WI.prev + '</span><span class="wd-pg-box" id="pv-count">1 of 2</span><span class="wd-pg-btn wd-pg-next">' + WI.next + '</span>' +
      '<span class="wd-zoom"><span>43%</span><span class="wd-zb">−</span><span class="wd-zslider"><i></i></span><span class="wd-zb">+</span><span class="wd-zb">' + WI.fit + '</span></span></div></div>';
    return '<div class="w11-page wd-bs-page" data-page="print">' + col + preview + '</div>';
  }

  /* ================================ 6. Demos ================================ */

  /* w1-scale: Settings ▸ System ▸ Display ▸ Scale 125% (ported from mockup 2). */
  DL2Demo.define({
    id: 'w1-scale', title: 'Change display scale in Settings', start: [640, 420],
    scene: '<div class="w11-wall"></div>' +
      win('Settings', 'gear16', '<div class="w11-body">' + settingsNav('System') + '<div class="w11-content">' + SYSTEM_PAGE + DISPLAY_PAGE + '</div></div>', 'w11-settings') +
      taskbar(['start', 'search', 'explorer', 'edge', 'settings'], 'settings'),
    steps: [
      { check: 'System page', cap: 'Settings is open to the <em>System</em> page.', state: { attr: { page: 'system' } } },
      { check: 'Click Display', cap: 'Click <em>Display</em>.', target: '#card-display', action: 'click', at: [0.3, 0.5], state: { attr: { page: 'display' } } },
      { check: 'Open Scale', cap: 'Under Scale &amp; layout, open the <em>Scale</em> menu.', target: '#scale-dd', action: 'click', state: { cls: { 'menu-open': true } } },
      { check: 'Choose 125%', cap: 'Choose <em>125%</em>. Everything gets bigger, right away.', target: '#opt-125', action: 'click', zoomOut: true,
        state: { cls: { 'menu-open': false }, css: { '--ui': '17.5px' }, text: { '#scale-val': '125%' } } },
      { check: 'Check, then undo', cap: 'Check each app. To undo it, choose <em>100%</em> again.' }
    ]
  });

  /* w1-sound: taskbar speaker ▸ Quick Settings ▸ Select a sound output ▸ Headphones. */
  DL2Demo.define({
    id: 'w1-sound', title: 'Send sound to your headset', start: [700, 380],
    scene: desktop([{ icon: 'bin', label: 'Recycle Bin' }, { icon: 'folder', label: 'Class Files' }]) + quickSettings() +
      taskbar(['start', 'search', 'explorer', 'edge']),
    steps: [
      { check: 'Headset plugged in', cap: 'Plug your headset in first. Sound is still going to the speakers.', state: { attr: { qs: 'closed', out: 'speakers' } } },
      { check: 'Click the speaker', cap: 'Click the <em>speaker</em> icon on the taskbar.', target: '#tray-sound', action: 'click', at: [0.75, 0.8], state: { attr: { qs: 'open' } } },
      { check: 'Open outputs', cap: 'Click the arrow beside the volume slider.', target: '#qs-output', action: 'click', at: [0.7, 0.72], state: { attr: { qs: 'outputs' } } },
      { check: 'Pick headphones', cap: 'Choose <em>Headphones</em>.', target: '#out-headphones', action: 'click', at: [0.84, 0.55], state: { attr: { out: 'headphones' } } },
      { check: 'Test it', cap: 'Play a sound. It should be in your headset now.', target: '#out-headphones', action: 'hover', at: [0.84, 0.55], zoom: false }
    ]
  });

  /* w1-print: Word ▸ File ▸ Print ▸ Normal Margins ▸ Narrow, so the flyer fits on one page. */
  DL2Demo.define({
    id: 'w1-print', title: 'Fit a flyer on one printed page in Word', start: [900, 330],
    scene: '<div class="w11-wall"></div>' + wordWin('Community Supper Flyer.docx', '<div class="wd-backstage">' + wordRail() + printPage() + '</div>') +
      taskbar(['start', 'search', 'explorer', 'edge', 'word'], 'word'),
    steps: [
      { check: 'Open Print', cap: 'Press <kbd>Ctrl</kbd> + <kbd>P</kbd> (or File ▸ Print) to see the preview.', state: { attr: { page: 'print', margins: 'normal' } } },
      { check: 'Spot the spill', cap: 'The preview says <em>1 of 2</em>. One line spilled onto page 2.', target: '#pv-count', action: 'hover', at: [0.92, 0.75] },
      { check: 'Open margins', cap: 'Under Settings, click <em>Normal Margins</em>.', target: '#margins-dd', action: 'click', at: [0.6, 0.32], state: { cls: { 'menu-open': true } } },
      { check: 'Choose Narrow', cap: 'Choose <em>Narrow</em>.', target: '#m-narrow', action: 'click', at: [0.82, 0.5], zoomOut: true,
        state: { cls: { 'menu-open': false }, attr: { margins: 'narrow' }, text: { '#pv-count': '1 of 1', '#margins-val': 'Narrow Margins' } } },
      { check: 'Print one test copy', cap: 'One page now. Print <em>one</em> test copy first.', target: '#print-btn', action: 'click', at: [0.78, 0.3] }
    ]
  });

  /* Append further Week 1 demos (w1-calendar, w1-autocorrect) here, reusing taskbar(), caption(),
   * wordWin() and wordRail() (the rail highlights [data-rail="account"] on data-page="account"). */
})();
