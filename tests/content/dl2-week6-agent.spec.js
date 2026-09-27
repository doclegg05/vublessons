// Week 6 redesign (2026-09-26): an instructor-led AI coding agent demo. Learners write the spec and
// checks, review the agent's diff, test three practice pages and retest after the repair.
// Sources: scripts/dl2/author-content.py, build-pages.py, photo_scenes.py, scenes.py, workshops.py,
// courses/digital-literacy-2/assets/workshop.js and courses/digital-literacy-2/activities/*.html.
const {test,expect}=require('@playwright/test');const fs=require('fs');
const read=p=>fs.readFileSync(p,'utf8');
const course='courses/digital-literacy-2';
const w6=JSON.parse(read('scripts/dl2/curriculum.json')).weeks[5];
const week=f=>read(`${course}/weeks/week-06/${f}`);
const activity=f=>read(`${course}/activities/${f}`);
const text=html=>html.replace(/<[^>]+>/g,' ').replace(/&lt;/g,'<').replace(/&gt;/g,'>').replace(/&#x27;/g,"'").replace(/&quot;/g,'"').replace(/&amp;/g,'&').replace(/\s+/g,' ');
const esc=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#x27;');
function section(html,n){const m=html.match(new RegExp(`<section[^>]*id="slide-${n}"[^>]*>([\\s\\S]*?)</section>`));if(!m)throw new Error(`slide-${n} not found`);return m[1];}
const count=(s,word)=>s.split(word).length-1;
// The inline script of a practice page, one array entry per source line.
const script=html=>html.split('<script>\n')[1].split('</script>')[0].split('\n');
const changed=(a,b)=>{const x=script(a),y=script(b);expect(x.length).toBe(y.length);return x.map((l,i)=>[l,y[i]]).filter(([l,r])=>l!==r);};
const v1=()=>activity('resource-finder.html'),v2=()=>activity('resource-finder-agent.html'),v3=()=>activity('resource-finder-agent-fixed.html');

test('Week 6 teaches directing an AI coding agent, not vibe coding',()=>{
 expect(w6.title).toBe('Guide an AI agent to improve a web app');
 expect(w6.summary).toBe('Write a clear request for an AI coding agent, review what it changed, test the result, and learn what running a website as a service takes.');
 expect(w6.refs).toEqual(['Extension: agentic engineering basics and SaaS']);
 const learner=JSON.stringify([w6.title,w6.summary,w6.objectives,w6.slides,w6.lab,w6.procedures,w6.glossary]);
 expect(learner).not.toMatch(/vibe coding|approved AI tool|Community Skills Desk/i);
 // Learners hear "an AI coding agent"; tool names belong only in instructor prep and notes.
 expect(learner).not.toMatch(/Claude|ChatGPT|Copilot|Cursor|Gemini/);
});

test('Week 6 slide titles name each step of the agent loop; order, count and kinds are unchanged',()=>{
 expect(w6.slides.map(s=>s.title)).toEqual(['Solve one small problem','Website, web app, and SaaS','An AI coding agent works in a loop','Three parts of a browser app','Write acceptance checks first','Write a spec the agent can follow','Ask the agent for a plan first','Start with a working reference','Review the change: read the diff','Make one change at a time','Write a useful repair request','Where does the data live?','Keep secrets out of browser code','A mock sign-in is not security','Watch: prompt, test, revise','Test more than the happy path','Report the bug; check for a regression','Hosting is a separate decision','Knowledge check: AI confidence','Knowledge check: a secret key','Lab: spec, review, test, explain','You can direct an agent and judge its work']);
 expect(w6.slides.map(s=>s.kind)).toEqual(['discussion','teach','teach','flip','steps','prompt','teach','starter','try','teach','teach','teach','teach','teach','video','steps','teach','teach','check','check','lab','summary']);
});

test('Week 6 slide 10 shows the agent’s diff, with minus and plus signs, where toLowerCase disappears',()=>{
 const s=section(week('presentation.html'),10);
 expect(s).toContain('Review the change: read the diff');
 expect(s).toContain('<del>- const query=search.value.trim().toLowerCase();</del>');
 expect(s).toContain('<ins>+ const query=search.value.trim();</ins>');
 expect(s).toMatch(/<ins>\+ [^<]*r\.name\+' '\+r\.category\+' '\+r\.description/);
 expect(s).toMatch(/<ins>\+ placeholder="Try library or learning"<\/ins>/);
 expect(s).not.toMatch(/Community Skills Desk|Find a resource|Community resources/);
});

test('Slide 10’s diff lines are real lines of versions 1 and 2',()=>{
 const s=text(section(week('presentation.html'),10));
 const pairs=changed(v1(),v2()).map(([a,b])=>[a.trim(),b.trim()]);
 expect(pairs).toHaveLength(2);
 expect(pairs[0]).toEqual(['const query=search.value.trim().toLowerCase();','const query=search.value.trim();']);
 expect(pairs[1][0]).toContain("(r.name+' '+r.description)");expect(pairs[1][1]).toContain("(r.name+' '+r.category+' '+r.description)");
 expect(s).toContain("- (r.name+' '+r.description)");expect(s).toContain("+ (r.name+' '+r.category+' '+r.description)");
 expect(v1()).toContain('placeholder="Try library"');expect(v2()).toContain('placeholder="Try library or learning"');
});

test('The three practice pages: version 2 keeps its planted defect and version 3 is a one-line repair',()=>{
 // Ctrl+U then Ctrl+F for toLowerCase: 2 places in versions 1 and 3, 1 place in version 2.
 expect(count(v1(),'toLowerCase')).toBe(2);expect(count(v2(),'toLowerCase')).toBe(1);expect(count(v3(),'toLowerCase')).toBe(2);
 expect(v2()).toContain('const query=search.value.trim();');
 expect(count(v2(),'trim()')).toBe(1);
 const repair=changed(v2(),v3());
 expect(repair).toEqual([['  const query=search.value.trim();','  const query=search.value.trim().toLowerCase();']]);
 expect(v1()).toContain('<title>Fictional community resource finder</title>');
 expect(v2()).toContain('<title>Fictional community resource finder · version 2 (agent result)</title>');
 expect(v3()).toContain('<title>Fictional community resource finder · version 3 (after the repair)</title>');
 const about='A real service would need verified resources and a plan for updates.</p>';
 expect(v2()).toContain(about+'<p><strong>Version 2.</strong> Changed by an AI coding agent. Review and test it before you trust it.</p>');
 expect(v3()).toContain(about+'<p><strong>Version 3.</strong> The agent repaired the capital-letter search. Retest it before you trust it.</p>');
 for(const page of [v1(),v2(),v3()]){
  expect(page).toMatch(/^const resources=\[$/m);
  expect(page).toContain('<script src="/shared/text-size.js"></script>');
  expect(page).toContain('<h1>Community resource finder</h1>');
 }
});

test('Version 1’s script has one statement per line, so an agent’s diff is short enough to read',()=>{
 const lines=script(v1());
 expect(lines).toContain('  const query=search.value.trim().toLowerCase();');
 expect(lines).toContain('search.addEventListener(\'input\',render);');
 expect(lines).toContain('category.addEventListener(\'change\',render);');
 for(const line of lines)expect(line.length,line).toBeLessThanOrEqual(170);
});

test('Week 6 worksheet opens all three versions and gives the procedures before the tasks',()=>{
 const ws=week('worksheet.html');
 for(const f of ['resource-finder.html','resource-finder-agent.html','resource-finder-agent-fixed.html'])expect(ws).toContain(`href="/courses/digital-literacy-2/activities/${f}"`);
 expect(ws).toContain('href="/courses/digital-literacy-2/activities/resource-finder.html" download="resource-finder-v1.html"');
 expect(ws).toContain('href="/courses/digital-literacy-2/activities/resource-finder-agent.html" download="resource-finder-v2.html"');
 for(const label of ['Open version 1','Open the agent’s version','Open the repaired version'])expect(ws).toContain(`>${label}</a>`);
 const firstTask=ws.indexOf('<h2>1. ');
 for(const [title,steps] of w6.procedures){
  expect(ws.indexOf(esc(title))).toBeGreaterThan(0);expect(ws.indexOf(esc(title))).toBeLessThan(firstTask);
  for(const step of steps)expect(ws).toContain(esc(step));
 }
 expect(w6.procedures.map(p=>p[0])).toEqual(['Open the three versions (no account needed)','Check the change yourself (no AI account needed)','Optional: repair version 2 by hand']);
 expect(text(ws)).not.toMatch(/Community Skills Desk|resource-finder-ai\.html|approved AI tool/);
});

test('Week 6 worksheet logs the five checks and the retest, with a typed box for each result',()=>{
 const ws=week('worksheet.html'),plain=text(ws);
 expect(plain).toMatch(/App test log Open the agent’s version \(resource-finder-agent\.html\)\. [^.]*\. Check What to do Expected Actual Pass or fail/);
 expect(plain).toMatch(/Retest after the repair [^]*? Check What to do Expected Actual Pass or fail/);
 for(const [check,todo] of [['Happy path, new','type learning'],['Happy path, still works','type library'],['No match','type zzz'],['Mixed case','type LIBRARY, then Learning'],['Keyboard only','Tab through every control'],['Narrow screen','zoom to 400%']])expect(plain).toContain(`${check} ${todo}`);
 expect(plain).toContain('Retest after the repair');
 for(const row of ['The check that failed','Passed before: learning','Passed before: zzz'])expect(plain).toContain(row);
 expect(ws.match(/<textarea class="worksheet-input" id="log-\d+-\d"/g)).toHaveLength(18);
 expect(ws.match(/<textarea class="worksheet-input" id="retest-\d+-\d"/g)).toHaveLength(9);
 expect(ws.indexOf('<h2>App test log</h2>')).toBeGreaterThan(ws.indexOf('<h2>8. '));
});

test('Week 6 rubric scores four criteria 0, 1 or 2 with descriptors, on the worksheet and the answer guide',()=>{
 expect(w6.rubric).toHaveLength(4);
 for(const row of w6.rubric){expect(row).toHaveLength(4);for(const cell of row)expect(cell.length).toBeGreaterThan(8);}
 expect(w6.rubric.map(r=>r[0])).toEqual(['Spec and checks','Prediction and review','Testing and retest','SaaS trade-offs']);
 expect(w6.rubric[0][3]).toBe('One clear change, what must stay the same, and three checks a partner can run');
 for(const page of [week('worksheet.html'),week('answer-key.html')]){
  const plain=text(page);
  expect(plain).toContain('Criterion 0 1 2 Score');
  for(const [criterion,...levels] of w6.rubric){expect(plain).toContain(criterion);for(const level of levels)expect(plain).toContain(level);}
  expect(plain).toContain('Total __ / 8');
 }
});

test('Week 6 answer guide lists the expected result of every check',()=>{
 const plain=text(week('answer-key.html'));
 for(const expected of ['learning, 2 fictional resources found (Community library, Practice Workbook Workshop), pass','zzz, No matching resources. Try a different word or reset the filters., pass','LIBRARY and Learning, No matching resources instead of 1 and 2 found, fail','LIBRARY: 1 found (Community library), pass','Learning: 2 found, pass'])expect(plain).toContain(expected);
});

test('Week 6 transcript defines the words the video uses, above the transcript',()=>{
 const html=week('video-transcript.html'),plain=text(html);
 expect(w6.glossary.map(g=>g[0])).toEqual(['Agent','Prompt','Spec','Acceptance check','Happy path','Diff','Regression','Hosting','SaaS (software as a service)','API key','Authentication']);
 expect(plain).toContain('Words in this video');
 for(const [term,definition] of w6.glossary){expect(plain).toContain(term);expect(plain).toContain(definition);}
 expect(html.indexOf('Words in this video')).toBeLessThan(html.indexOf('id="transcript-content"'));
 for(let n=1;n<=5;n++)expect(read(`${course}/weeks/week-0${n}/video-transcript.html`)).not.toContain('Words in this video');
});

test('Week 6 plan, syllabus and instructor guide describe the instructor-led agent demo',()=>{
 const plan=text(week('lesson-plan.html'));
 expect(plan).toContain('For week 6, the instructor runs an AI coding agent on the projector; learners need no account or AI access. Supply a plain-text editor for the optional hand repair.');
 expect(plan).not.toMatch(/approved AI tool/);
 const syllabus=text(read(`${course}/syllabus.html`));
 expect(syllabus).toContain('IC3 Digital Literacy GS6 Level 2 + AI Agent and SaaS Basics');
 expect(syllabus).toContain('Spec, change review and test log.');
 expect(syllabus).toContain('In the final week the instructor demonstrates an AI coding agent; learners write the request, review the change and test it, with no account or AI access of their own.');
 expect(syllabus).not.toMatch(/approved AI tool|Web App Building|Prototype and test log/);
 const guide=text(read(`${course}/instructor-guide.html`));
 expect(guide).toContain('Rehearse the week 6 agent demo and open the three practice pages (versions 1, 2 and 3).');
 expect(guide).not.toContain('Download the starter HTML for the account-free week 6 path.');
});

test('Week 6 slides show the real starter page and the agent loop, not the old rename or focus repair',()=>{
 const deck=week('presentation.html');
 for(const stale of ['Community Skills Desk','Find a resource','Learning desk','Learning Desk','Computer help desk','Neighborhood center','Community Library','Only the heading changes','focus-practice','Focus is hard to see','resource-finder-v2.html','vibe coding'])expect(deck,stale).not.toContain(stale);
 expect(deck).toContain('&lt;h1&gt;Community resource finder&lt;/h1&gt;');
 for(const row of ['Community library · Learning','Community Makers Group · Community','Practice Workbook Workshop · Learning'])expect(deck).toContain(row);
 expect(text(section(deck,12))).toMatch(/Repair request .*LIBRARY and Learning find nothing; library and learning work/);
 expect(text(section(deck,18))).toContain('Open version 2; type LIBRARY');
 expect(text(section(deck,17))).toContain('Test version 2 (resource-finder-agent.html); write what actually happens');
 const js=read(`${course}/assets/workshop.js`);
 expect(js).toContain('<h1>Community resource finder</h1>');
 expect(js).toContain('Change request for the AI coding agent: ${task}.');
 expect(js).toContain('Show me your plan before you change anything, then list every line you changed.');
 expect(js).not.toMatch(/Computer help desk|Neighborhood center|Find a resource|Build a one-page app/);
});
