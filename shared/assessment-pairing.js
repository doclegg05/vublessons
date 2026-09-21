/* Explicit, attempt-specific comparisons for assessments on shared workstations. */
(function () {
  'use strict';
  window.VUBAssessmentPairing = function (options) {
    const root = document.getElementById('assessmentPairing');
    const nameInput = document.getElementById('participantName');
    const instructorInput = document.getElementById('instructorName');
    let savedText = null;
    let candidate = null;
    let confirmed = null;
    let revealed = false;
    const normalize = value => String(value || '').trim().replace(/\s+/g, ' ').toLocaleLowerCase();
    const read = () => {
      try { return localStorage.getItem(options.preKey); } catch (_) { return null; }
    };
    savedText = read();
    try { candidate = JSON.parse(savedText); } catch (_) { /* No usable baseline. */ }
    if (!candidate || typeof candidate.name !== 'string' || !candidate.name.trim() ||
        !Number.isFinite(candidate.score) || candidate.score < 0 || candidate.score > 100) candidate = null;
    root.innerHTML = '<h3>Optional pre-test comparison</h3>' +
      '<p id="pairingSummary"></p>' +
      '<button type="button" id="findPretest">Find my saved pre-test</button>' +
      '<label class="pairing-choice"><input type="checkbox" id="confirmPretest">' +
      '<span>I recognize this saved attempt as my own pre-test. Compare it with my post-test.</span></label>' +
      '<p id="pairingStatus" role="status"></p>' +
      '<button type="button" id="clearPretest">New learner: clear saved assessment results</button>';
    const checkbox = document.getElementById('confirmPretest');
    const summary = document.getElementById('pairingSummary');
    const status = document.getElementById('pairingStatus');
    function update() {
      const matches = candidate && normalize(nameInput.value) === normalize(candidate.name);
      checkbox.disabled = !matches || !revealed;
      checkbox.closest('label').hidden = !revealed || !candidate;
      document.getElementById('findPretest').hidden = revealed || !candidate;
      summary.textContent = candidate && !revealed ? 'If you took your pre-test on this browser, you can review the saved attempt before choosing a comparison.' : candidate
        ? 'Saved pre-test: ' + candidate.name + ' · ' + (candidate.date || 'date unavailable') + ' · ' + candidate.score + '%.'
        : 'No usable pre-test is saved on this workstation.';
      status.textContent = candidate && !revealed ? 'Comparison is optional. You can begin without looking up a pre-test.' : !candidate
        ? 'Continue with your post-test. No comparison will be included.'
        : !matches
          ? 'Enter your own name above. Only confirm if this is your attempt; matching names alone do not identify a learner. Leave unchecked to continue without a comparison.'
          : confirmed
            ? 'Your selected pre-test will be compared. Changing your name or instructor clears this selection.'
            : 'Check the saved name, date, and score. If you cannot identify this as your own attempt, leave unchecked and ask your instructor to compare your reports.';
    }
    function revoke() { confirmed = null; checkbox.checked = false; update(); }
    nameInput.addEventListener('input', revoke);
    instructorInput.addEventListener('input', revoke);
    document.getElementById('findPretest').addEventListener('click', function () { revealed = true; update(); });
    checkbox.addEventListener('change', function () {
      if (read() !== savedText) { candidate = null; revoke(); return; }
      confirmed = checkbox.checked && candidate && normalize(nameInput.value) === normalize(candidate.name)
        ? { name: nameInput.value.trim(), instructor: instructorInput.value.trim(), confirmedAt: new Date().toISOString() }
        : null;
      update();
    });
    document.getElementById('clearPretest').addEventListener('click', function () {
      let cleared = true;
      try { localStorage.removeItem(options.preKey); localStorage.removeItem(options.postKey); } catch (_) { cleared = false; }
      candidate = null; savedText = null; revoke();
      status.textContent = cleared
        ? 'Saved results for this course were cleared from this browser. Enter your own name and continue without a comparison.'
        : 'Comparison was cleared for this assessment, but browser storage could not be cleared. Ask your instructor before leaving this shared workstation.';
      nameInput.value = ''; instructorInput.value = ''; nameInput.focus();
    });
    window.addEventListener('storage', function (event) {
      if (event.key === options.preKey || event.key === null) { candidate = null; revoke(); }
    });
    update();
    return {
      getConfirmed: function () {
        if (!confirmed || !candidate || read() !== savedText ||
            nameInput.value.trim() !== confirmed.name || instructorInput.value.trim() !== confirmed.instructor ||
            normalize(nameInput.value) !== normalize(candidate.name)) return null;
        return { score: candidate.score, name: candidate.name, date: candidate.date || null,
          timestamp: candidate.timestamp || null, confirmedAt: confirmed.confirmedAt };
      }
    };
  };
}());
