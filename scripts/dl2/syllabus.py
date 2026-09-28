"""Print-friendly DL2 syllabus, following the Level 1 syllabus overview format."""
from html import escape


def render(weeks):
    dates = ['September 28', 'October 5', 'October 12', 'October 19', 'October 26', 'November 2']
    outcomes = '\n'.join(
        '<li>' + ' '.join(escape(x) for x in w['objectives']) + '</li>'
        for w in weeks
    )
    rows = []
    for w, date in zip(weeks, dates):
        evidence = {1: 'Pre-test.', 5: 'Post-test and skills challenge.', 6: 'Spec, change review and test log.'}.get(w['n'], '')
        alignment = 'VUB web app extension' if w['n'] == 6 else 'GS6 objective groups: ' + ', '.join(w['refs'])
        rows.append(f'''<tr>
          <th scope="row">Week {w['n']}<br><span>{date}</span></th>
          <td>{escape(w['title'])}</td>
          <td>{escape(w['summary'])} <strong>{evidence}</strong><br><em>{escape(alignment)}</em></td>
        </tr>''')
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Six-week VUB Digital Literacy Level 2 syllabus, schedule, learning outcomes and materials.">
  <title>VUB Syllabus — Digital Literacy: Level 2 (IC3 GS6 Aligned)</title>
  <link rel="stylesheet" href="/courses/digital-literacy-2/assets/syllabus.css">
  <script src="/shared/text-size.js" defer></script>
  <script src="/courses/digital-literacy-2/assets/syllabus.js" defer></script>
</head>
<body>
  <a class="skip" href="#main">Skip to syllabus</a>
  <nav class="document-actions" aria-label="Syllabus tools">
    <a href="/courses/digital-literacy-2/index.html">Course home</a>
    <button type="button" id="print-syllabus">Print / Save as PDF</button>
  </nav>
  <main id="main">
    <header class="header">
      <div class="letterhead">
        <img class="letterhead-logo" src="/assets/VUB%20Logo.png" width="120" height="120" alt="Veterans Upward Bound for West Virginia logo">
        <div class="letterhead-name">
          <p class="letterhead-region">West Virginia</p>
          <p class="organization">Veterans Upward Bound</p>
          <p class="letterhead-motto">Building technology confidence for veterans.</p>
        </div>
      </div>
      <div class="course-heading">
      <p class="document-label">Course syllabus</p>
      <h1>Digital Literacy — Level 2</h1>
      <p class="subtitle">IC3 Digital Literacy GS6 Level 2 + AI Agent and SaaS Basics</p>
      <p class="info"><strong>Schedule:</strong> Mondays, September 28–November 2, 2026<br>
      4:30–6:30 p.m. Eastern Time · Six meetings · 12 contact hours<br>
      Computer lab instruction</p>
      <p class="instructor-contact"><strong>Instructor:</strong> Britt Legg<br>
      <strong>Email:</strong> <a href="mailto:britt.legg76@gmail.com">britt.legg76@gmail.com</a></p>
      </div>
    </header>
    <section aria-labelledby="description">
      <h2 id="description">Course Description</h2>
      <p>This six-week course builds practical digital skills for veterans, aligned with <strong>IC3 GS6 Level 2</strong>. Five weeks cover everyday technology, information, content creation, communication, collaboration and safety. A sixth week extends that learning through basic AI-assisted web app building.</p>
      <p>For veterans who can use a mouse and keyboard, open a browser and manage basic files. Level 1 or equivalent experience is recommended. Ask the instructor for a refresher when needed.</p>
    </section>
    <section aria-labelledby="outcomes">
      <h2 id="outcomes">Learning Outcomes (IC3 GS6 Level 2 + VUB Extension)</h2>
      <ul class="outcomes">{outcomes}</ul>
    </section>
    <section aria-labelledby="learning">
      <h2 id="learning">How We Will Learn</h2>
      <p>Each meeting combines demonstration, a short captioned explainer, guided practice, individual tasks, partner feedback and a check for understanding. Use fictional examples throughout. In the final week the instructor demonstrates an AI coding agent; learners write the request, review the change and test it, with no account or AI access of their own.</p>
    </section>
    <section class="schedule" aria-labelledby="schedule">
      <h2 id="schedule">Course Schedule</h2>
      <table>
        <caption>All meetings: 4:30–6:30 p.m. Eastern Time · 2026</caption>
        <thead><tr><th scope="col">Week / Date</th><th scope="col">Lesson</th><th scope="col">Key Activities &amp; Alignment</th></tr></thead>
        <tbody>{''.join(rows)}</tbody>
      </table>
      <p class="schedule-note">The October 12 meeting is included as scheduled. Confirm building access with the program before that meeting.</p>
    </section>
    <section aria-labelledby="assessment">
      <h2 id="assessment">Assessment &amp; Materials</h2>
      <p>The <strong>Pre-Test (Week 1)</strong> occurs before instruction; the <strong>Post-Test (Week 5)</strong> follows the GS6 lessons. Each has 20 questions across the seven IC3 domains, with the same counts on both forms, and produces a graded results PDF and submits a copy for the instructor through Netlify. The tests use different questions covering the same skills. The Week 6 prototype uses a separate 8-point rubric. Scores guide practice; they are not certification results.</p>
      <p><strong>Materials:</strong> A workstation, browser, headphones, word processor, spreadsheet app and plain-text editor support the activities. Captions, transcripts, keyboard navigation, text sizing and print copies are available. The calendar task can use an instructor demonstration account or a paper simulation. No real purchases, private records or paid AI account are needed.</p>
    </section>
    <section aria-labelledby="practice">
      <h2 id="practice">Between Meetings</h2>
      <p>Optional: repeat one class task with fictional data and note where you need help. Save your worksheets and assessment results before leaving a shared computer.</p>
    </section>
  </main>
  <footer>WV Veterans Upward Bound · Building technology confidence for veterans.</footer>
</body>
</html>
'''
