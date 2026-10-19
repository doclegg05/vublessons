// Week 6 (guide an agent): the rebuilt deck uses the three prepared app versions, teaches the roadblocks between a
// page on your computer and a real service, and uses current wording about agents and keys.
// Shared rebuilt-week checks are in dl2-rebuilt-weeks.spec.js; the app versions are pinned in dl2-week6-agent.spec.js.
// Source: scripts/dl2/mission-control/week6.py and scripts/dl2/curriculum.json; regenerate before running.
// DL2_ROOT points the checks at another copy of the repository (for example an export of an older commit).
const {test,expect}=require('@playwright/test');const fs=require('fs');const path=require('path');
const root=process.env.DL2_ROOT||'.';
const read=p=>fs.readFileSync(path.join(root,p),'utf8');
const dir='courses/digital-literacy-2/weeks/week-06/';
const plain=html=>html.replace(/<[^>]+>/g,' ').replace(/&amp;/g,'&').replace(/&#x27;/g,"'").replace(/&quot;/g,'"').replace(/\s+/g,' ');
const deckHtml=read(dir+'presentation.html'),deck=plain(deckHtml),sheet=plain(read(dir+'worksheet.html'));

test('The deck opens the three prepared versions in new tabs from the missions that use them',()=>{
 for(const f of ['resource-finder.html','resource-finder-agent.html','resource-finder-agent-fixed.html'])
  expect(deckHtml).toContain(`href="/courses/digital-literacy-2/activities/${f}" target="_blank"`);
});

test('Mission 6D teaches the roadblocks between a local page and a real service',()=>{
 for(const word of ['Domain name','Hosting','Back end','sign-in','Secret keys','Caretaker'])expect(deck.toLowerCase()).toContain(word.toLowerCase());
 expect(sheet).toContain('Roadblock cards');
});

test('Agents and keys are described as they work now',()=>{
 for(const page of [deck,sheet])expect(page).not.toMatch(/approve each step|map service|such as maps/i);
 expect(plain(read(dir+'video-transcript.html'))).toContain('you review every change before you accept it');
});

test('The opening video no longer carries the old alignment warning',()=>{
 expect(deck).not.toMatch(/Existing alignment limitation/);
});
