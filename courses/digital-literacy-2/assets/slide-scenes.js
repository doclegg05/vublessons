/* Local teaching examples: never request permissions, send messages or collect data. */
(() => {
  'use strict';
  document.querySelectorAll('[data-topic-scene]').forEach(scene => {
    scene.querySelectorAll('[data-scene-choice]').forEach(button => button.addEventListener('click', () => {
      scene.querySelectorAll('[data-scene-choice]').forEach(b => b.setAttribute('aria-pressed', String(b === button)));
      scene.querySelectorAll('[data-scene-state]').forEach(panel => { panel.hidden = panel.dataset.sceneState !== button.dataset.sceneChoice; });
    }));
  });
  document.querySelectorAll('[data-step-done]').forEach(button => button.addEventListener('click', () => {
    const done = button.getAttribute('aria-pressed') !== 'true';
    button.setAttribute('aria-pressed', String(done));
    button.querySelector('.step-state').textContent = done ? 'Practiced · select to undo' : 'Mark practiced';
  }));
  const chart = document.querySelector('[data-chart-lab]');
  chart?.querySelectorAll('[data-chart]').forEach(button => button.addEventListener('click', () => {
    const mode = button.dataset.chart; const paper = mode === 'changed' ? 15 : 12;
    const bars = chart.querySelector('.bar-chart');
    chart.querySelectorAll('[data-chart]').forEach(b => b.setAttribute('aria-pressed', String(b === button)));
    const order = mode === 'sorted' ? ['Pens', 'Folders', 'Paper'] : ['Paper', 'Folders', 'Pens'];
    order.forEach(name => bars.append(chart.querySelector(`[data-item="${name}"]`)));
    const row = chart.querySelector('[data-item="Paper"]');
    row.querySelector('.bar-track span').style.width = `${paper / 15 * 100}%`;
    row.querySelector('b').textContent = `$${paper}`;
    bars.setAttribute('aria-label', `Paper ${paper} dollars, Folders 8 dollars, Pens 5 dollars`);
    chart.querySelector('[data-chart-paper]').textContent = paper;
    chart.querySelector('[data-chart-insight]').textContent = mode === 'changed' ? 'Paper now costs $15. The bar and data table both change; the scale stays the same.' : mode === 'sorted' ? 'Pens cost the least: $5. Reordering changes the reading order, not the values.' : 'Paper costs the most: $12. Compare bar lengths from the same zero baseline.';
  }));
  const crop = document.querySelector('[data-crop-lab]');
  crop?.querySelectorAll('[data-crop]').forEach(button => button.addEventListener('click', () => {
    const mode = button.dataset.crop;
    crop.querySelectorAll('[data-crop]').forEach(b => b.setAttribute('aria-pressed', String(b === button)));
    crop.dataset.mode = mode;
    crop.querySelector('[data-crop-note]').textContent = {original:'The original stays available. Save an edited copy under a different name.', crop:'Crop removes the outer areas. The center remains at the original scale; check that important content and credit are not lost.', resize:'Resize changes the dimensions while preserving the whole image and its proportions. Nothing is stretched.'}[mode];
  }));
  const trim = document.querySelector('[data-trim-lab]');
  trim?.querySelectorAll('[data-trim]').forEach(button => button.addEventListener('click', () => {
    const mode = button.dataset.trim;
    trim.querySelectorAll('[data-trim]').forEach(b => b.setAttribute('aria-pressed', String(b === button)));
    trim.querySelectorAll('[data-clip]').forEach(clip => {
      const removed = mode === 'trim' && clip.dataset.clip === 'edge' || mode === 'split' && clip.dataset.clip === 'middle';
      clip.classList.toggle('clip-removed', removed);
      clip.setAttribute('aria-label', `${clip.textContent}${removed ? ' — removed' : ' — kept'}`);
    });
    trim.querySelector('[data-trim-note]').textContent = {original:'Original duration: 20 seconds. Choose an edit and compare what remains.', trim:'Trim removes 3 seconds at each end. The remaining clip lasts 14 seconds.', split:'Split at 9 and 12 seconds, then remove the 3-second pause. The remaining clip lasts 17 seconds.'}[mode];
  }));
})();
