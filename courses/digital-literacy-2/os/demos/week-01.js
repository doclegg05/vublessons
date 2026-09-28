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
 *   5. Word kit                wordWin(), wordRail(), printPage(), docView(), accountPage(), aboutDialog()
 *   6. Outlook kit             outlookWin(), calendarView(), eventForm()
 *   7. Demos                   DL2Demo.define(...) — append new demos at the end of this section. */
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

  /* Word document view: tabs, the Home ribbon (Word 2408, classic ribbon on a rounded card), the page and
   * the status bar. `#doc-line` is the typed line; its caret is a ::after so textContent writes keep it. */
  var WR = {
    paste: svg(32, '0 0 32 32', '<rect x="5" y="6" width="16" height="20" rx="2" fill="#f4ead6" stroke="#8a6d3b" stroke-width="1.2"/><rect x="9" y="3.5" width="8" height="5" rx="1.2" fill="#fff" stroke="#616161" stroke-width="1.2"/>' +
      '<rect x="13" y="12" width="14" height="17" rx="1.5" fill="#fff" stroke="#424242" stroke-width="1.2"/>' + line('M16 17h8M16 20.5h8M16 24h5', 1.1, '#616161')),
    cut: svg(16, '0 0 16 16', '<circle cx="4.5" cy="12" r="2" fill="none" stroke="currentColor" stroke-width="1.1"/><circle cx="11.5" cy="12" r="2" fill="none" stroke="currentColor" stroke-width="1.1"/>' + line('M5.8 10.4L11 2.5M10.2 10.4L5 2.5', 1.1)),
    copy: svg(16, '0 0 16 16', line('M5.5 4.5V3a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1h-1.5M3.5 5.5a1 1 0 0 1 1-1h5a1 1 0 0 1 1 1v8a1 1 0 0 1-1 1h-5a1 1 0 0 1-1-1z', 1.1)),
    painter: svg(16, '0 0 16 16', line('M3 2.5h9v3.5H3zM12 4.2h1.5V8H7.5v2', 1.1) + '<rect x="6.3" y="10" width="2.4" height="4.5" rx=".6" fill="#c9a227"/>'),
    grow: svg(16, '0 0 16 16', line('M2 13.5L6 3l4 10.5M3.4 10h5.2', 1.2) + line('M11 6l2-2 2 2', 1.1)),
    shrink: svg(16, '0 0 16 16', line('M2 13.5L6 3l4 10.5M3.4 10h5.2', 1.2) + line('M11 4l2 2 2-2', 1.1)),
    clear: svg(16, '0 0 16 16', line('M2 13.5L6 3l4 10.5M3.4 10h5.2', 1.2) + '<path d="M10 11.5l3-3 2 2-3 3z" fill="#f4a3c4" stroke="#b4235a" stroke-width=".8"/>'),
    effects: svg(16, '0 0 16 16', '<path d="M2.5 14L7 2h2l4.5 12h-2.3l-1-2.8H5.8l-1 2.8zM6.5 9.3h3L8 5z" fill="#dbe8fb" stroke="#185abd" stroke-width=".9"/>'),
    highlight: svg(16, '0 0 16 16', line('M5 9.5l5.5-6.5 2.6 2.6-6.4 5.6zM5 9.5l-1.2 2.6 2.6-1.1', 1.1) + '<rect x="1.5" y="13" width="13" height="2.3" fill="#ffff00" stroke="#b8b800" stroke-width=".4"/>'),
    color: svg(16, '0 0 16 16', line('M3.5 11L7.5 1.5h1L12.5 11M5 7.5h6', 1.2) + '<rect x="1.5" y="13" width="13" height="2.3" fill="#ff0000"/>'),
    bullets: svg(16, '0 0 16 16', '<circle cx="3" cy="4" r="1.1" fill="currentColor"/><circle cx="3" cy="8" r="1.1" fill="currentColor"/><circle cx="3" cy="12" r="1.1" fill="currentColor"/>' + line('M6 4h8M6 8h8M6 12h8', 1.1)),
    numbering: svg(16, '0 0 16 16', '<text x="1" y="5.8" font-size="4.8" font-family="Segoe UI, sans-serif" fill="currentColor">1</text><text x="1" y="9.8" font-size="4.8" font-family="Segoe UI, sans-serif" fill="currentColor">2</text><text x="1" y="13.8" font-size="4.8" font-family="Segoe UI, sans-serif" fill="currentColor">3</text>' + line('M6 4h8M6 8h8M6 12h8', 1.1)),
    multi: svg(16, '0 0 16 16', '<circle cx="2.5" cy="3.5" r="1" fill="currentColor"/><circle cx="5.5" cy="8" r="1" fill="currentColor"/><circle cx="8.5" cy="12.5" r="1" fill="currentColor"/>' + line('M5 3.5h9M8 8h6M11 12.5h3', 1.1)),
    outdent: svg(16, '0 0 16 16', line('M2 3h12M8 6.5h6M8 10h6M2 13.5h12M5.5 6.5L3 8.2l2.5 1.7', 1.1)),
    indent: svg(16, '0 0 16 16', line('M2 3h12M8 6.5h6M8 10h6M2 13.5h12M3 6.5l2.5 1.7L3 10', 1.1)),
    sort: svg(16, '0 0 16 16', '<text x="1" y="7" font-size="6" font-family="Segoe UI, sans-serif" fill="currentColor">A</text><text x="1" y="14.5" font-size="6" font-family="Segoe UI, sans-serif" fill="currentColor">Z</text>' + line('M11.5 2.5v11M9 11l2.5 2.5L14 11', 1.1)),
    left: svg(16, '0 0 16 16', line('M2 3h12M2 6.3h8M2 9.6h12M2 12.9h8', 1.1)),
    center: svg(16, '0 0 16 16', line('M2 3h12M4 6.3h8M2 9.6h12M4 12.9h8', 1.1)),
    right: svg(16, '0 0 16 16', line('M2 3h12M6 6.3h8M2 9.6h12M6 12.9h8', 1.1)),
    justify: svg(16, '0 0 16 16', line('M2 3h12M2 6.3h12M2 9.6h12M2 12.9h12', 1.1)),
    spacing: svg(16, '0 0 16 16', line('M7 3h7M7 6.3h7M7 9.6h7M7 12.9h7M3.5 2.5v11M2 4l1.5-1.5L5 4M2 12l1.5 1.5L5 12', 1.1)),
    shading: svg(16, '0 0 16 16', line('M3 7.5L8 2.5l4.5 4.5-5 5z', 1.1) + '<path d="M13.2 8.5s1.3 1.6 1.3 2.4a1.3 1.3 0 0 1-2.6 0c0-.8 1.3-2.4 1.3-2.4z" fill="currentColor"/>'),
    borders: svg(16, '0 0 16 16', '<path d="M2.5 2.5h11v11h-11z" fill="none" stroke="currentColor" stroke-width="1" stroke-dasharray="1.2 1.3"/>' + line('M2 13.5h12', 1.6)),
    find: svg(16, '0 0 16 16', '<circle cx="6.8" cy="6.8" r="4.3" fill="none" stroke="currentColor" stroke-width="1.2"/>' + line('M10 10l4 4', 1.3)),
    replace: svg(16, '0 0 16 16', '<text x="1" y="7" font-size="6" font-family="Segoe UI, sans-serif" fill="currentColor">ab</text><text x="7.5" y="14.5" font-size="6" font-family="Segoe UI, sans-serif" fill="#185abd">ac</text>' + line('M3 9.5v2.5h3', 1)),
    select: svg(16, '0 0 16 16', '<path d="M4 2v10.5l2.8-2.6 1.9 4.1 1.8-.8-1.9-4h3.7z" fill="#fff" stroke="currentColor" stroke-width="1"/>'),
    mic: svg(28, '0 0 28 28', '<rect x="10" y="3" width="8" height="14" rx="4" fill="#fff" stroke="#424242" stroke-width="1.3"/>' + line('M6.5 13a7.5 7.5 0 0 0 15 0M14 20.5V25M10 25h8', 1.3, '#424242')),
    editor: svg(28, '0 0 28 28', line('M6 22l2-6L19 5l4 4L12 20zM16.5 7.5l4 4', 1.3, '#424242') + '<path d="M22 17l1 2.5 2.5 1-2.5 1-1 2.5-1-2.5-2.5-1 2.5-1z" fill="#185abd"/><path d="M8.5 22.5h13" stroke="#185abd" stroke-width="1.6" stroke-linecap="round"/>'),
    addins: svg(28, '0 0 28 28', '<rect x="4" y="4" width="8.5" height="8.5" rx="1.5" fill="none" stroke="#424242" stroke-width="1.3"/><rect x="4" y="15.5" width="8.5" height="8.5" rx="1.5" fill="none" stroke="#424242" stroke-width="1.3"/><rect x="15.5" y="15.5" width="8.5" height="8.5" rx="1.5" fill="none" stroke="#424242" stroke-width="1.3"/><rect x="15" y="3" width="8.5" height="8.5" rx="1.5" transform="rotate(45 19.25 7.25)" fill="#dbe8fb" stroke="#185abd" stroke-width="1.3"/>'),
    launch: svg(9, '0 0 10 10', line('M1 5V1h4M9 9L3.5 3.5M9 9V5.5M9 9H5.5', .9)),
    comment: svg(16, '0 0 16 16', line('M2.5 3.5a1 1 0 0 1 1-1h9a1 1 0 0 1 1 1v6.5a1 1 0 0 1-1 1H7l-3 2.5V11H3.5a1 1 0 0 1-1-1z', 1.1)),
    pen: svg(16, '0 0 16 16', line('M3 13l1-3.5L11 2.5l2.5 2.5-7 7zM9.5 4l2.5 2.5', 1.1)),
    share: svg(16, '0 0 16 16', line('M8 10V2.5M5.3 5L8 2.3 10.7 5M5 7.5H4a1 1 0 0 0-1 1v5a1 1 0 0 0 1 1h8a1 1 0 0 0 1-1v-5a1 1 0 0 0-1-1h-1', 1.1)),
    bolt: svg(14, '0 0 16 16', '<path d="M9.5 1.5L3.5 9h4l-1.5 5.5L12.5 7h-4z" fill="#fff4c4" stroke="#b07d00" stroke-width="1" stroke-linejoin="round"/>'),
    boltBlue: svg(16, '0 0 16 16', '<path d="M9.5 1.5L3.5 9h4l-1.5 5.5L12.5 7h-4z" fill="#dbe8fb" stroke="#185abd" stroke-width="1" stroke-linejoin="round"/>'),
    proof: svg(14, '0 0 16 16', line('M3 2.5h7.5a1 1 0 0 1 1 1V13a.5.5 0 0 1-.5.5H4a1 1 0 0 1-1-1zM3 11.5h8.5M6 6.3l1.4 1.4L10 5', 1.1)),
    access: svg(14, '0 0 16 16', '<circle cx="8" cy="3" r="1.3" fill="currentColor"/>' + line('M3 5.5l5 1.2 5-1.2M8 6.7v3l-2.3 4M8 9.7l2.3 4', 1.1)),
    vRead: svg(14, '0 0 16 16', line('M2 3.5h5a1 1 0 0 1 1 1v9a1 1 0 0 0-1-1H2zM14 3.5H9a1 1 0 0 0-1 1v9a1 1 0 0 1 1-1h5z', 1)),
    vPrint: svg(14, '0 0 16 16', line('M3.5 2h7l2 2v10h-9zM5.5 6.5h5M5.5 9h5M5.5 11.5h3', 1)),
    vWeb: svg(14, '0 0 16 16', '<circle cx="8" cy="8" r="6" fill="none" stroke="currentColor" stroke-width="1"/>' + line('M2 8h12M8 2c-2.5 3.5-2.5 8.5 0 12M8 2c2.5 3.5 2.5 8.5 0 12', 1))
  };
  function rbig(icon, label, dd) { return '<span class="wd-big">' + icon + '<span>' + label + (dd ? I.chevD : '') + '</span></span>'; }
  function rsm(icon, label, dd) { return '<span class="wd-sm">' + icon + (label ? '<span>' + label + '</span>' : '') + (dd ? I.chevD : '') + '</span>'; }
  function rib(icon, cls) { return '<span class="wd-ib' + (cls ? ' ' + cls : '') + '">' + icon + '</span>'; }
  function ribdd(icon) { return '<span class="wd-ib wd-ibdd">' + icon + I.chevD + '</span>'; }
  function grp(label, body, launch) {
    return '<div class="wd-grp"><div class="wd-grp-b">' + body + '</div><div class="wd-grp-l">' + label + (launch ? '<span class="wd-launch">' + WR.launch + '</span>' : '') + '</div></div>';
  }
  function styleTile(sample, name, cls, sel) {
    return '<span class="wd-st' + (sel ? ' sel' : '') + '"><span class="wd-st-s ' + cls + '">' + sample + '</span><span class="wd-st-n">' + name + '</span></span>';
  }
  function wordTabs() {
    var tabs = ['Home', 'Insert', 'Draw', 'Design', 'Layout', 'References', 'Mailings', 'Review', 'View', 'Help'];
    return '<div class="wd-tabs"><span class="wd-tab" id="file-tab">File</span>' + tabs.map(function (t) {
      return '<span class="wd-tab' + (t === 'Home' ? ' sel' : '') + '">' + t + '</span>';
    }).join('') + '<span class="wd-tabs-r"><span class="wd-tbtn">' + WR.comment + '<span>Comments</span></span><span class="wd-tbtn">' + WR.pen + '<span>Editing</span>' + I.chevD + '</span>' +
      '<span class="wd-tbtn">' + WR.share + '<span>Share</span>' + I.chevD + '</span></span></div>';
  }
  function homeRibbon() {
    var txt = function (t, cls) { return '<span class="wd-ib wd-glyph ' + (cls || '') + '">' + t + '</span>'; };
    return '<div class="wd-ribbon">' +
      grp('Undo', '<span class="wd-col">' + rsm(WI.undo, '', true) + rsm(WI.redo) + '</span>') +
      grp('Clipboard', rbig(WR.paste, 'Paste', true) + '<span class="wd-col">' + rsm(WR.cut) + rsm(WR.copy) + rsm(WR.painter) + '</span>', true) +
      grp('Font', '<span class="wd-col"><span class="wd-rrow"><span class="wd-combo wd-fname"><span>Aptos (Body)</span>' + I.chevD + '</span><span class="wd-combo wd-fsize"><span>12</span>' + I.chevD + '</span>' +
        rib(WR.grow) + rib(WR.shrink) + '<span class="wd-ib wd-ibdd wd-glyph">Aa' + I.chevD + '</span>' + rib(WR.clear) + '</span>' +
        '<span class="wd-rrow">' + txt('B', 'wd-bold') + txt('I', 'wd-ital') + '<span class="wd-ib wd-ibdd wd-glyph wd-under">U' + I.chevD + '</span>' + txt('ab', 'wd-strike') +
        txt('x<span class="wd-sub-s">2</span>') + txt('x<span class="wd-sup-s">2</span>') + '<span class="wd-rsep"></span>' + ribdd(WR.effects) + ribdd(WR.highlight) + ribdd(WR.color) + '</span></span>', true) +
      grp('Paragraph', '<span class="wd-col"><span class="wd-rrow">' + ribdd(WR.bullets) + ribdd(WR.numbering) + ribdd(WR.multi) + rib(WR.outdent) + rib(WR.indent) + rib(WR.sort) + txt('¶') + '</span>' +
        '<span class="wd-rrow">' + rib(WR.left, 'sel') + rib(WR.center) + rib(WR.right) + rib(WR.justify) + ribdd(WR.spacing) + ribdd(WR.shading) + ribdd(WR.borders) + '</span></span>', true) +
      grp('Styles', '<span class="wd-gallery">' + styleTile('AaBbCcDd', 'Normal', 'wd-sn', true) + styleTile('AaBbCcDd', 'No Spacing', 'wd-sn') +
        styleTile('AaBbCc', 'Heading 1', 'wd-sh1') + styleTile('AaBbCcD', 'Heading 2', 'wd-sh2') +
        '<span class="wd-gscroll"><span>' + WI.up + '</span><span>' + WI.down + '</span><span>' + WI.down + '</span></span></span>', true) +
      grp('Editing', '<span class="wd-col">' + rsm(WR.find, 'Find', true) + rsm(WR.replace, 'Replace') + rsm(WR.select, 'Select', true) + '</span>') +
      grp('Voice', rbig(WR.mic, 'Dictate', true)) + grp('Editor', rbig(WR.editor, 'Editor')) + grp('Add-ins', rbig(WR.addins, 'Add-ins')) + '</div>';
  }
  function docView() {
    return '<div class="wd-docview">' + wordTabs() + homeRibbon() +
      '<div class="wd-canvas"><div class="wd-page"><div class="wd-h1">Help Desk Note</div>' +
      '<div class="wd-p">To: Community Skills Desk</div><div class="wd-p">From: Veteran Learner, Lab PC 07</div>' +
      '<div class="wd-p">Word keeps changing what I type. Here is an example:</div>' +
      // The AutoCorrect layer re-types "Copyright " invisibly in the same font, so the blue mark and the
      // lightning button land exactly under the © on any machine's fonts.
      '<div class="wd-p wd-typed"><span id="doc-line"></span><span class="wd-acl"><span class="wd-ghost">Copyright </span><span class="wd-acmark"><span class="wd-ghost">©</span>' +
      '<span class="wd-acbtn" id="ac-button" title="AutoCorrect Options">' + WR.bolt + I.chevD +
      '<span class="w11-flyout wd-acmenu"><span class="wd-acm" id="ac-undo"><span class="wd-acm-ico"></span><span>Change back to "(c)"</span></span>' +
      '<span class="wd-acm"><span class="wd-acm-ico"></span><span>Stop Automatically Correcting "(c)"</span></span><span class="wd-acsep"></span>' +
      '<span class="wd-acm"><span class="wd-acm-ico">' + WR.boltBlue + '</span><span>Control AutoCorrect Options…</span></span></span></span></span></span></div>' +
      '</div></div>' +
      '<div class="wd-status"><span>Page 1 of 1</span><span id="wd-words">23 words</span><span class="wd-si">' + WR.proof + '</span><span>English (United States)</span>' +
      '<span>Text Predictions: On</span><span class="wd-si">' + WR.access + '<span>Accessibility: Good to go</span></span>' +
      '<span class="wd-status-r"><span>Focus</span><span class="wd-si">' + WR.vRead + '</span><span class="wd-si wd-vsel">' + WR.vPrint + '</span><span class="wd-si">' + WR.vWeb + '</span>' +
      '<span class="wd-zb">−</span><span class="wd-zslider wd-zs100"><i></i></span><span class="wd-zb">+</span><span>100%</span></span></div></div>';
  }
  /* File ▸ Account (backstage page) and the About Microsoft® Word dialog (data-about="open"). */
  var TILE = {
    update: svg(32, '0 0 32 32', '<rect x="5" y="5" width="22" height="22" rx="3" fill="#fff" stroke="#424242" stroke-width="1.3"/>' + line('M16 9v11M11.5 15.5L16 20l4.5-4.5M11 23.5h10', 1.4, '#185abd')),
    about: svg(32, '0 0 32 32', '<circle cx="16" cy="16" r="11" fill="#fff" stroke="#424242" stroke-width="1.3"/>' + line('M12.6 12.8a3.5 3.5 0 1 1 5 3.2c-1 .5-1.6 1.2-1.6 2.3v.9', 1.6, '#185abd') + '<circle cx="16" cy="22.6" r="1.2" fill="#185abd"/>'),
    news: svg(32, '0 0 32 32', '<path d="M16 4.5l2.6 7.2 7.4.3-5.8 4.7 2 7.3L16 19.8 9.8 24l2-7.3L6 12l7.4-.3z" fill="#fff" stroke="#424242" stroke-width="1.3" stroke-linejoin="round"/><circle cx="16" cy="15.2" r="2.2" fill="#185abd"/>')
  };
  function appTile(bg, letter) { return '<span class="wd-app" style="background:' + bg + '">' + letter + '</span>'; }
  function accountPage() {
    var tile = function (id, icon, label, title, lines) {
      return '<div class="wd-tilerow"><div class="wd-tile"' + (id ? ' id="' + id + '"' : '') + '>' + icon + '<span>' + label + '</span></div>' +
        '<div class="wd-tiletext"><b>' + title + '</b>' + lines.map(function (l) { return '<span>' + l + '</span>'; }).join('') + '</div></div>';
    };
    var ms = svg(30, '0 0 22 22', '<rect x="0" y="0" width="10.4" height="10.4" fill="#f25022"/><rect x="11.6" y="0" width="10.4" height="10.4" fill="#7fba00"/><rect x="0" y="11.6" width="10.4" height="10.4" fill="#00a4ef"/><rect x="11.6" y="11.6" width="10.4" height="10.4" fill="#ffb900"/>');
    return '<div class="w11-page wd-bs-page wd-acct" data-page="account"><div class="wd-h">Account</div><div class="wd-acct-cols">' +
      '<div class="wd-acct-l"><div class="wd-sub2">User Information</div><div class="wd-uav">VL</div><div class="wd-uname">Veteran Learner</div><div class="wd-umail">learner@example.org</div>' +
      '<div class="wd-link">Sign out</div><div class="wd-link">Switch account</div>' +
      '<div class="wd-lab">Office Background:</div><div class="wd-sel"><span>No Background</span>' + I.chevD + '</div>' +
      '<div class="wd-lab">Office Theme:</div><div class="wd-sel"><span>Use system setting</span>' + I.chevD + '</div>' +
      '<div class="wd-lab">Connected Services:</div><div class="wd-link">Add a service ▾</div></div>' +
      '<div class="wd-acct-r"><div class="wd-sub2">Product Information</div><div class="wd-ms">' + ms + '<span>Microsoft 365</span></div>' +
      '<div class="wd-prod"><b>Subscription Product</b><span>Microsoft 365 Apps for enterprise</span><span class="wd-small">This product contains</span>' +
      '<span class="wd-apps">' + appTile('#185abd', 'W') + appTile('#107c41', 'X') + appTile('#c43e1c', 'P') + appTile('#0f6cbd', 'O') + appTile('#7719aa', 'N') + '</span></div>' +
      '<div class="wd-btns"><span class="wd-btn">Manage Account</span><span class="wd-btn">Change License</span></div>' +
      tile('', TILE.update, 'Update Options ▾', 'Microsoft 365 and Office Updates', ['Updates are automatically downloaded and installed.']) +
      tile('about-word', TILE.about, 'About Word', 'About Word', ['Learn more about Word, Support, Product ID, and Copyright information.', 'Version 2408 (Build 17928.20114 Click-to-Run)', 'Current Channel']) +
      tile('', TILE.news, 'What\'s New', 'What\'s New', ['See the most recently installed updates.']) + '</div></div></div>';
  }
  function aboutDialog() {
    return '<div class="wd-about" role="dialog" aria-label="About Microsoft Word"><div class="wd-about-t"><span>About Microsoft® Word</span>' +
      '<span class="wd-about-x">' + svg(10, '0 0 10 10', '<path d="M.5.5l9 9M9.5.5l-9 9" stroke="currentColor" stroke-width="1"/>') + '</span></div>' +
      '<div class="wd-about-b"><div class="wd-about-top">' + I.word +
      '<div class="wd-about-lines"><div id="about-version">Microsoft® Word for Microsoft 365 MSO (Version 2408 Build 16.0.17928.20114) 64-bit</div>' +
      '<div>Product ID: 00000-00000-00000-AA000</div><div class="wd-link">Third-party notices</div></div></div>' +
      '<div class="wd-about-lic"><div>Microsoft 365 Apps for enterprise</div><div>This product is licensed under the Microsoft Software License Terms.</div>' +
      '<div>© Microsoft Corporation. All rights reserved.</div></div><div class="wd-about-ok"><span class="wd-okbtn">OK</span></div></div></div>';
  }

  /* ============================== 6. Outlook kit ============================== */
  /* New Outlook for Windows (2024–26), Neutral theme: Mica header and app bar, white cards and the
   * #0f6cbd accent. Calendar ▸ Week view, 8 AM – 7 PM at OL_HR px per hour. data-week="2" swaps the
   * week-1 labels/events (.ol-t1/.ol-e1) for week 2 (.ol-t2/.ol-e2); data-saved="yes" shows VUB class. */
  var OL_HR = 37;
  var OI = {
    mail: svg(20, '0 0 20 20', line('M2.5 5.8A1.8 1.8 0 0 1 4.3 4h11.4a1.8 1.8 0 0 1 1.8 1.8v8.4a1.8 1.8 0 0 1-1.8 1.8H4.3a1.8 1.8 0 0 1-1.8-1.8zM3 6l7 5 7-5', 1.3)),
    calSel: svg(20, '0 0 20 20', '<path d="M2.5 6A2.5 2.5 0 0 1 5 3.5h10A2.5 2.5 0 0 1 17.5 6v8.5A2.5 2.5 0 0 1 15 17H5a2.5 2.5 0 0 1-2.5-2.5z" fill="currentColor"/><path d="M2.5 7.5h15" stroke="#fff" stroke-width="1.2"/>' +
      '<circle cx="6.6" cy="10.6" r="1" fill="#fff"/><circle cx="10" cy="10.6" r="1" fill="#fff"/><circle cx="13.4" cy="10.6" r="1" fill="#fff"/><circle cx="6.6" cy="13.8" r="1" fill="#fff"/><circle cx="10" cy="13.8" r="1" fill="#fff"/>'),
    people: svg(20, '0 0 20 20', line('M7.5 9.3a2.9 2.9 0 1 0 0-5.8 2.9 2.9 0 0 0 0 5.8zM2.5 16.5c0-2.6 2.2-4.3 5-4.3s5 1.7 5 4.3M13 3.8a2.7 2.7 0 0 1 0 5.2M14.6 12.4c1.8.5 2.9 1.9 2.9 4.1', 1.3)),
    todo: svg(20, '0 0 20 20', '<circle cx="10" cy="10" r="7" fill="none" stroke="currentColor" stroke-width="1.3"/>' + line('M6.8 10.2l2.2 2.2 4.3-4.6', 1.3)),
    cloud: svg(20, '0 0 20 20', '<path d="M5.2 15.5h10.3a3.2 3.2 0 0 0 .3-6.4 4.7 4.7 0 0 0-9-1.1 3.8 3.8 0 0 0-1.6 7.5z" fill="#0f6cbd"/>'),
    apps: svg(20, '0 0 20 20', '<rect x="3" y="3" width="6" height="6" rx="1.5" fill="none" stroke="currentColor" stroke-width="1.3"/><rect x="11" y="3" width="6" height="6" rx="1.5" fill="none" stroke="currentColor" stroke-width="1.3"/><rect x="3" y="11" width="6" height="6" rx="1.5" fill="none" stroke="currentColor" stroke-width="1.3"/>' + line('M14 11v6M11 14h6', 1.3)),
    ham: svg(18, '0 0 20 20', line('M3 5.5h14M3 10h14M3 14.5h14', 1.3)),
    calAdd: svg(18, '0 0 20 20', line('M3 5.5A2 2 0 0 1 5 3.5h10a2 2 0 0 1 2 2V10M3 5.5v9a2 2 0 0 0 2 2h4.5M3 7.5h14M14.5 12v6M11.5 15h6', 1.4)),
    cal: svg(18, '0 0 20 20', line('M3 5.5A2 2 0 0 1 5 3.5h10a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2zM3 7.5h14', 1.3) + '<circle cx="7" cy="10.8" r=".95" fill="currentColor"/><circle cx="10" cy="10.8" r=".95" fill="currentColor"/><circle cx="13" cy="10.8" r=".95" fill="currentColor"/><circle cx="7" cy="13.6" r=".95" fill="currentColor"/><circle cx="10" cy="13.6" r=".95" fill="currentColor"/>'),
    day: svg(18, '0 0 20 20', line('M3 5.5A2 2 0 0 1 5 3.5h10a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2zM3 7.5h14', 1.3) + '<rect x="7.5" y="9.5" width="5" height="5" rx=".8" fill="currentColor"/>'),
    wwk: svg(18, '0 0 20 20', line('M3 5.5A2 2 0 0 1 5 3.5h10a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2zM3 7.5h14M6 10v4.5M8.7 10v4.5M11.3 10v4.5M14 10v4.5', 1.3)),
    week: svg(18, '0 0 20 20', line('M3 5.5A2 2 0 0 1 5 3.5h10a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2zM3 7.5h14M7.3 7.5v9M12.7 7.5v9', 1.3)),
    month: svg(18, '0 0 20 20', line('M3 5.5A2 2 0 0 1 5 3.5h10a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2zM3 7.5h14M3 12h14M7.3 7.5v9M12.7 7.5v9', 1.3)),
    share: svg(18, '0 0 20 20', line('M10 12.5V3.5M6.8 6.5L10 3.3l3.2 3.2M6 9H5a1.5 1.5 0 0 0-1.5 1.5v5A1.5 1.5 0 0 0 5 17h10a1.5 1.5 0 0 0 1.5-1.5v-5A1.5 1.5 0 0 0 15 9h-1', 1.3)),
    print: svg(18, '0 0 20 20', line('M6 7.5V3.5h8v4M6 14H4.5a1 1 0 0 1-1-1V8.5a1 1 0 0 1 1-1h11a1 1 0 0 1 1 1V13a1 1 0 0 1-1 1H14M6 11.5h8v5H6z', 1.3)),
    today: svg(16, '0 0 20 20', line('M3 5.5A2 2 0 0 1 5 3.5h10a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2zM3 7.5h14', 1.4) + '<rect x="5.8" y="10" width="3.6" height="3.6" rx=".6" fill="currentColor"/>'),
    save: svg(16, '0 0 20 20', line('M4 4.5a1 1 0 0 1 1-1h8.5L16 6v9.5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1zM7 3.5v4h5.5v-4M6.5 16.5v-5h7v5', 1.4)),
    trash: svg(18, '0 0 20 20', line('M4 5.5h12M8 5.5V4a1 1 0 0 1 1-1h2a1 1 0 0 1 1 1v1.5M5.5 5.5l.8 10.2a1.5 1.5 0 0 0 1.5 1.3h4.4a1.5 1.5 0 0 0 1.5-1.3l.8-10.2M8.5 8.5v5.5M11.5 8.5v5.5', 1.3)),
    busy: svg(18, '0 0 20 20', '<rect x="3.5" y="3.5" width="13" height="13" rx="2.5" fill="none" stroke="currentColor" stroke-width="1.3"/><rect x="6.5" y="6.5" width="7" height="7" rx="1" fill="#0f6cbd"/>'),
    bell: svg(18, '0 0 20 20', line('M10 2.8a4.6 4.6 0 0 0-4.6 4.6v3.4L4 13.8h12l-1.4-3V7.4A4.6 4.6 0 0 0 10 2.8zM8 15.8a2.1 2.1 0 0 0 4 0', 1.3)),
    sched: svg(18, '0 0 20 20', line('M7 8.5a2.5 2.5 0 1 0 0-5 2.5 2.5 0 0 0 0 5zM2.5 15.5c0-2.3 2-3.9 4.5-3.9 1 0 2 .3 2.7.7', 1.3) + '<circle cx="14" cy="13.5" r="3.7" fill="none" stroke="currentColor" stroke-width="1.3"/>' + line('M14 11.7v2l1.3.9', 1.2)),
    tag: svg(18, '0 0 20 20', line('M3.5 4.5a1 1 0 0 1 1-1h5l7 7-6 6-7-7z', 1.3) + '<circle cx="7" cy="7" r="1.2" fill="currentColor"/>'),
    respond: svg(18, '0 0 20 20', line('M3.5 6.5A1.5 1.5 0 0 1 5 5h10a1.5 1.5 0 0 1 1.5 1.5v7A1.5 1.5 0 0 1 15 15H5a1.5 1.5 0 0 1-1.5-1.5zM4 6l6 4.3L16 6', 1.3)),
    lock: svg(18, '0 0 20 20', line('M6.5 9V7a3.5 3.5 0 0 1 7 0v2M5 9h10v7.5H5z', 1.3)),
    clock: svg(20, '0 0 20 20', '<circle cx="10" cy="10" r="7" fill="none" stroke="currentColor" stroke-width="1.3"/>' + line('M10 6v4.3l2.8 1.8', 1.3)),
    repeat: svg(20, '0 0 20 20', line('M15.8 8.5A6 6 0 0 0 5 6.3M4.6 3.3v3.2h3.2M4.2 11.5A6 6 0 0 0 15 13.7M15.4 16.7v-3.2h-3.2', 1.3)),
    repeatSm: svg(12, '0 0 20 20', line('M15.8 8.5A6 6 0 0 0 5 6.3M4.6 3.3v3.2h3.2M4.2 11.5A6 6 0 0 0 15 13.7M15.4 16.7v-3.2h-3.2', 2)),
    pin: svg(20, '0 0 20 20', line('M10 17.5s-5.3-4.9-5.3-9a5.3 5.3 0 0 1 10.6 0c0 4.1-5.3 9-5.3 9z', 1.3) + '<circle cx="10" cy="8.4" r="1.9" fill="none" stroke="currentColor" stroke-width="1.3"/>'),
    personAdd: svg(20, '0 0 20 20', line('M8 9a3 3 0 1 0 0-6 3 3 0 0 0 0 6zM2.5 16.5c0-2.8 2.4-4.6 5.5-4.6 1 0 1.9.2 2.7.5M15 11.5v5M12.5 14h5', 1.3)),
    titleCal: svg(20, '0 0 20 20', '<path d="M3 6a2.5 2.5 0 0 1 2.5-2.5h9A2.5 2.5 0 0 1 17 6v8.5a2.5 2.5 0 0 1-2.5 2.5h-9A2.5 2.5 0 0 1 3 14.5z" fill="#0f6cbd"/><path d="M3 7.5h14" stroke="#fff" stroke-width="1.2"/>'),
    check: svg(14, '0 0 16 16', line('M3 8.5l3.2 3.2L13 4.8', 1.5)),
    up: svg(12, '0 0 12 12', line('M3 7.5L6 4.5l3 3', 1.2)),
    down: svg(12, '0 0 12 12', line('M3 4.5L6 7.5l3-3', 1.2))
  };
  function olBtn(icon, label, cls, dd) {
    return '<span class="ol-b' + (cls ? ' ' + cls : '') + '">' + (icon || '') + (label ? '<span>' + label + '</span>' : '') + (dd ? I.chevD : '') + '</span>';
  }
  function olTabs(tabs, sel) {
    return '<div class="ol-tabs"><span class="ol-ham">' + OI.ham + '</span>' + tabs.map(function (t) {
      return '<span class="ol-tab' + (t === sel ? ' sel' : '') + '">' + t + '</span>';
    }).join('') + '</div>';
  }
  function outlookWin(body) {
    var apps = [['mail', ''], ['calSel', ' sel'], ['people', ''], ['todo', ''], ['cloud', '']];
    return '<div class="ol-win"><div class="ol-top"><span class="ol-appico">' + I.outlook + '</span>' +
      '<span class="ol-search">' + WI.search + '<span>Search</span></span>' +
      '<span class="ol-topr"><span class="ol-tico">' + I.bell + '</span><span class="ol-tico">' + I.gear18 + '</span><span class="ol-av">VL</span></span>' + caption(true, 'ol-ctl') + '</div>' +
      '<div class="ol-main"><div class="ol-appbar">' + apps.map(function (a) { return '<span class="ol-app' + a[1] + '">' + OI[a[0]] + '</span>'; }).join('') +
      '<span class="ol-app ol-app-more">' + OI.apps + '</span></div><div class="ol-stage">' + body + '</div></div></div>';
  }
  /* The folder pane: the mini month (September for week 1, October for week 2, with the shown week
   * highlighted and today, Sep 28, circled) and the calendar list. lead = first weekday of the month. */
  function miniMonth(title, lead, days, prevLast, today, week, cls) {
    var rows = '';
    for (var r = 0; r < 6; r++) {
      rows += '<div class="ol-mr' + (r === week ? ' ol-mwk' : '') + '">';
      for (var k = r * 7; k < r * 7 + 7; k++) {
        var n = k - lead + 1, d = n < 1 ? prevLast + n : n > days ? n - days : n;
        rows += '<span class="' + (n < 1 || n > days ? 'ol-out' : '') + (k === today ? ' ol-mtoday' : '') + '">' + d + '</span>';
      }
      rows += '</div>';
    }
    return '<div class="ol-mini ' + cls + '"><div class="ol-mini-h"><span>' + title + '</span><span class="ol-mini-arr">' + OI.up + OI.down + '</span></div>' +
      '<div class="ol-mr ol-mdow"><span>S</span><span>M</span><span>T</span><span>W</span><span>T</span><span>F</span><span>S</span></div>' + rows + '</div>';
  }
  function folderPane() {
    var cb = function (color, label, on) {
      return '<div class="ol-calrow"><span class="ol-cb' + (on ? '' : ' off') + '" style="--c:' + color + '">' + (on ? OI.check : '') + '</span><span>' + label + '</span></div>';
    };
    return '<div class="ol-fold">' + miniMonth('September 2026', 2, 30, 31, 29, 4, 'ol-t1') + miniMonth('October 2026', 4, 31, 30, 1, 1, 'ol-t2') +
      '<div class="ol-fl-add">' + OI.calAdd + '<span>Add calendar</span></div><div class="ol-fl-h">' + I.chevD + '<span>My calendars</span></div>' +
      cb('#0f6cbd', 'Calendar', true) + cb('#8a8a8a', 'Birthdays', false) + cb('#13a10e', 'United States holidays', true) + '</div>';
  }
  function olEvent(cls, day, start, hours, title, extra) {
    return '<div class="ol-ev ' + cls + '" data-day="' + day + '" style="top:' + (start - 8) * OL_HR + 'px;height:' + (hours * OL_HR - 2) + 'px"><b>' + title + '</b>' + (extra || '') + '</div>';
  }
  var OL_DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
  var OL_WEEKS = [[27, 28, 29, 30, 1, 2, 3], [4, 5, 6, 7, 8, 9, 10]];
  // One-off events [css class, day index, start hour, hours, title]; VUB class is the only recurring one.
  var OL_EVENTS = [['ol-e1', 2, 10, 1, 'Doctor visit'], ['ol-e1', 4, 12, 1, 'Family lunch'], ['ol-e2', 3, 10.5, 1, 'Haircut']];
  function calendarView() {
    var head = '<div class="ol-dayhead"><span class="ol-gut"></span>' + OL_DAYS.map(function (d, k) {
      return '<span class="ol-dh' + (k === 1 ? ' ol-today' : '') + '"><b><span class="ol-t1">' + OL_WEEKS[0][k] + '</span><span class="ol-t2">' + OL_WEEKS[1][k] + '</span></b><span>' + d + '</span></span>';
    }).join('') + '</div>';
    var hours = ['8 AM', '9 AM', '10 AM', '11 AM', '12 PM', '1 PM', '2 PM', '3 PM', '4 PM', '5 PM', '6 PM', '7 PM'];
    var cols = OL_DAYS.map(function (d, k) {
      var evs = OL_EVENTS.filter(function (e) { return e[1] === k; }).map(function (e) { return olEvent(e[0], k, e[2], e[3], e[4]); }).join('');
      if (k === 1) evs += olEvent('ol-vub', k, 16.5, 2, 'VUB class', '<span class="ol-rep" title="Recurring event">' + OI.repeatSm + '</span>');
      return '<div class="ol-col' + (k === 0 || k === 6 ? ' ol-wkend' : '') + '">' + evs + '</div>';
    }).join('');
    return '<div class="ol-tabs-wrap">' + olTabs(['Home', 'View', 'Help'], 'Home') + '</div>' +
      '<div class="ol-cmd"><span class="ol-b ol-primary ol-split" id="new-event">' + OI.calAdd + '<span>New event</span><span class="ol-splitchev">' + I.chevD + '</span></span><span class="ol-sep"></span>' +
      olBtn(OI.day, 'Day') + olBtn(OI.wwk, 'Work week') + olBtn(OI.week, 'Week', 'sel') + olBtn(OI.month, 'Month') + '<span class="ol-sep"></span>' + olBtn(OI.share, 'Share') + olBtn(OI.print, 'Print') + '</div>' +
      '<div class="ol-content">' + folderPane() + '<div class="ol-card"><div class="ol-surf"><span class="ol-b ol-bordered">' + OI.today + '<span>Today</span></span>' +
      '<span class="ol-nav" title="Go to previous week">' + I.chevL + '</span><span class="ol-nav" id="next-week" title="Go to next week">' + I.chevR + '</span>' +
      '<span class="ol-range"><span class="ol-t1">September 27 – October 3, 2026</span><span class="ol-t2">October 4 – 10, 2026</span>' + I.chevD + '</span></div>' +
      head + '<div class="ol-grid"><div class="ol-hours">' + hours.map(function (h) { return '<span>' + h + '</span>'; }).join('') + '</div><div class="ol-cols">' + cols + '</div></div></div></div>';
  }
  /* The full New event form (data-form="open"): its own ribbon, the fields, and the day on the right. */
  function eventForm() {
    var rep = ['Don\'t repeat', 'Daily', 'Weekly on Monday', 'Monthly on the fourth Monday', 'Yearly on September 28', 'Custom'];
    var menu = '<div class="w11-flyout ol-menu">' + rep.map(function (r, k) {
      return '<div class="ol-opt' + (k === 0 ? ' sel' : '') + '"' + (k === 2 ? ' id="rep-weekly"' : '') + '><span class="ol-ck">' + OI.check + '</span><span>' + r + '</span></div>';
    }).join('') + '</div>';
    var row = function (icon, body) { return '<div class="ol-row"><span class="ol-ri">' + icon + '</span>' + body + '</div>'; };
    var fields = '<div class="ol-fields">' +
      row(OI.titleCal, '<div class="ol-title" id="ev-title" data-ph="Add a title"></div>') +
      row(OI.personAdd, '<div class="ol-in" id="ev-attendees"><span class="ol-ph">Invite required attendees</span><span class="ol-chip"><span class="ol-cav">P</span><span>partner@example.org</span></span></div><span class="ol-optl">Optional</span>') +
      row(OI.clock, '<span class="ol-box">Mon 9/28/2026' + OI.today + '</span><span class="ol-box">4:30 PM' + I.chevD + '</span><span class="ol-to">to</span><span class="ol-box">6:30 PM' + I.chevD + '</span>' +
        '<span class="ol-sw"><i></i><span>All day</span></span>') +
      row(OI.repeat, '<div class="ol-box ol-dd" id="ev-repeat" title="Make recurring"><span id="ev-repeat-val">Don\'t repeat</span>' + I.chevD + menu + '</div>') +
      row(OI.pin, '<div class="ol-in"><span class="ol-ph">Add a location</span></div>') +
      '<div class="ol-desc">Add a description or attach documents</div></div>';
    var dhours = ['1 PM', '2 PM', '3 PM', '4 PM', '5 PM', '6 PM', '7 PM', '8 PM'];
    var dayv = '<div class="ol-dayv"><div class="ol-dayv-h"><span class="ol-nav">' + I.chevL + '</span><span>Mon, September 28, 2026</span><span class="ol-nav">' + I.chevR + '</span></div>' +
      '<div class="ol-dayv-g">' + dhours.map(function (h) { return '<span>' + h + '</span>'; }).join('') + '<div class="ol-draft">4:30 PM – 6:30 PM</div></div></div>';
    return '<div class="ol-form">' + '<div class="ol-tabs-wrap">' + olTabs(['Event', 'Insert', 'Format text', 'Draw', 'Options'], 'Event') + '</div>' +
      '<div class="ol-cmd"><span class="ol-b ol-primary" id="ev-save">' + OI.save + '<span>Save</span></span>' + olBtn(OI.trash, 'Discard') + '<span class="ol-sep"></span>' +
      olBtn(OI.busy, 'Busy', '', true) + '<span class="ol-b" id="ev-remind" aria-label="Remind me: 15 minutes before">' + OI.bell + '<span>15 minutes before</span>' + I.chevD + '</span>' +
      olBtn(OI.sched, 'Scheduling Assistant') + olBtn(OI.tag, 'Categorize', '', true) + olBtn(OI.respond, 'Response options', '', true) + olBtn(OI.lock, 'Private') + '</div>' +
      '<div class="ol-fbody">' + fields + dayv + '</div></div>';
  }

  /* Word AutoCorrect turns "(c)" into "©" the moment the closing parenthesis is typed. The engine's type
   * action appends one character at a time, so watch #doc-line and make the same swap while it types.
   * Only a line that ENDS in "(c)" changes, so "Change back" (which leaves "(c) 2026") stays put. */
  if (window.MutationObserver) {
    new MutationObserver(function (list) {
      list.forEach(function (m) {
        var t = m.target;
        if (t.id === 'doc-line' && /\(c\)$/.test(t.textContent)) t.textContent = t.textContent.replace(/\(c\)$/, '©');
      });
    }).observe(document.documentElement, { childList: true, subtree: true });
  }

  /* ================================ 7. Demos ================================ */

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

  /* w1-calendar: new Outlook ▸ Calendar ▸ New event ▸ Repeat weekly ▸ Save ▸ next week. */
  DL2Demo.define({
    id: 'w1-calendar', title: 'Put a weekly class on your Outlook calendar', start: [760, 430],
    scene: '<div class="w11-wall"></div>' + outlookWin(calendarView() + eventForm()) + taskbar(['start', 'search', 'explorer', 'edge', 'outlook'], 'outlook'),
    steps: [
      { check: 'Calendar open', cap: 'Outlook is open to <em>Calendar</em>, Week view.', state: { attr: { form: 'closed', week: '1', saved: 'no', invite: 'no' } } },
      { check: 'New event', cap: 'Click <em>New event</em>.', target: '#new-event', action: 'click', at: [0.62, 0.8], state: { attr: { form: 'open' } } },
      { check: 'Add a title', cap: 'Type a clear title.', target: '#ev-title', action: 'type', text: 'VUB class', at: [0.24, 0.8], state: { text: { '#ev-title': 'VUB class' } } },
      { check: 'Make it repeat', cap: 'Open the <em>Repeat</em> menu.', target: '#ev-repeat', action: 'click', at: [0.8, 0.75], zoom: 1.7, state: { cls: { 'menu-open': true } } },
      { check: 'Weekly on Monday', cap: 'Choose <em>Weekly on Monday</em>.', target: '#rep-weekly', action: 'click', at: [0.8, 0.6],
        state: { cls: { 'menu-open': false }, text: { '#ev-repeat-val': 'Weekly on Monday' }, attr: { invite: 'yes' } } },
      { check: 'Invite and save', cap: 'Invite your partner, keep the 15-minute reminder, then <em>Save</em>.', target: '#ev-save', action: 'click', at: [0.72, 0.8], zoomOut: true,
        state: { attr: { form: 'closed', saved: 'yes' } } },
      { check: 'Check next week', cap: 'Click the next-week arrow. Is it on <em>Monday</em>?', target: '#next-week', action: 'click', at: [0.66, 0.78], zoomOut: true, state: { attr: { week: '2' } } }
    ]
  });

  /* w1-autocorrect: Word turns (c) into ©; AutoCorrect Options ▸ Change back; File ▸ Account ▸ About Word.
   * Step 5 clicks the File tab: the Account page (and #about-word) is hidden until File opens, and the
   * engine needs every target on screen when its step plays. The About Word tile shows pressed. */
  DL2Demo.define({
    id: 'w1-autocorrect', title: 'Undo an AutoCorrect change and find your Word version', start: [980, 600],
    scene: '<div class="w11-wall"></div>' + wordWin('Help Desk Note.docx', docView() + '<div class="wd-backstage">' + wordRail() + accountPage() + '</div>' + aboutDialog()) +
      taskbar(['start', 'search', 'explorer', 'edge', 'word'], 'word'),
    steps: [
      { check: 'Word open', cap: 'A note in Word. Watch what happens when we type <em>(c)</em>.', state: { attr: { page: 'doc', ac: 'none', about: 'closed' } } },
      { check: 'Type (c)', cap: 'Type <em>Copyright (c) 2026</em>.', target: '#doc-line', action: 'type', text: 'Copyright (c) 2026', at: [0.85, 1.3],
        state: { text: { '#doc-line': 'Copyright © 2026', '#wd-words': '26 words' }, attr: { ac: 'shown' } } },
      { check: 'Spot the change', cap: 'Word changed <em>(c)</em> into <em>©</em>. That\'s AutoCorrect.', target: '#ac-button', action: 'click', at: [0.5, 0.6], state: { cls: { 'menu-open': true } } },
      { check: 'Change it back', cap: 'Choose <em>Change back</em>. (Or press <kbd>Ctrl</kbd> + <kbd>Z</kbd> right away.)', target: '#ac-undo', action: 'click', at: [0.9, 0.6],
        state: { cls: { 'menu-open': false }, text: { '#doc-line': 'Copyright (c) 2026' }, attr: { ac: 'none' } } },
      { check: 'Find the version', cap: 'For a help request: File ▸ Account ▸ <em>About Word</em>.', target: '#file-tab', action: 'click', at: [0.62, 0.78], zoomOut: true,
        state: { attr: { page: 'account', about: 'open' } } },
      { check: 'Copy the version', cap: 'Write down the version number you see (ours says 2408; yours may be newer).', target: '#about-version', action: 'hover', at: [0.56, 1.1], zoom: 2.4 }
    ]
  });
})();
