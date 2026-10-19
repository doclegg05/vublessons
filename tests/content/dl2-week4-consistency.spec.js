// Week 4 (work together): one fictional cast, one feedback example and one offer pair across the deck,
// the worksheet and the answer key. Shared rebuilt-week checks are in dl2-rebuilt-weeks.spec.js.
// Source: scripts/dl2/mission-control/week4.py and scripts/dl2/curriculum.json; regenerate before running.
// DL2_ROOT points the checks at another copy of the repository (for example an export of an older commit).
const {test,expect}=require('@playwright/test');const fs=require('fs');const path=require('path');
const root=process.env.DL2_ROOT||'.';
const read=p=>fs.readFileSync(path.join(root,p),'utf8');
const dir='courses/digital-literacy-2/weeks/week-04/';
const plain=html=>html.replace(/<[^>]+>/g,' ').replace(/&amp;/g,'&').replace(/&#x27;/g,"'").replace(/&quot;/g,'"').replace(/\s+/g,' ');
const deck=plain(read(dir+'presentation.html')),sheet=plain(read(dir+'worksheet.html')),key=plain(read(dir+'answer-key.html'));

test('The review request goes to the reviewer with the organizer copied; Bcc is only for the volunteer notice',()=>{
 expect(deck).toContain('Review: To Sam · Cc Pat');
 expect(deck).toContain('Notice: To Alex · Cc Pat · Bcc volunteers');
 expect(key).toContain('To: Sam. Cc: Pat.');
 expect(key).toContain('To: Alex. Cc: Pat. Bcc: the 20 volunteers');
 expect(deck).not.toMatch(/To: Alex · Cc: Sam · Bcc: volunteers/);
});

test('One feedback example: in step 2, add where the learning desk is',()=>{
 expect(deck).toContain('In step 2, add where the desk is');
 expect(key).toContain('In step 2, add where the desk is');
 expect(key).not.toMatch(/opening hours/);
});

test('One offer pair, with a free trial: A is free for 30 days then $6 a month, B is $60 a year',()=>{
 for(const page of [deck,sheet])expect(page).toMatch(/free (for )?30 days, then \$6 a month/);
 expect(sheet).toContain('$60 a year');
 expect(key).toContain('$66 for 12 months');
 for(const page of [deck,sheet,key])expect(page).not.toMatch(/\$5 ?(\/|a )month|\$48/);
});

test('Zelle is described as part of a bank app, not a standalone app',()=>{
 expect(sheet).toContain('Zelle in your bank');
});

test('The meeting and checkout simulations are the Mission 4C and 4D practice pages',()=>{
 expect(read(dir+'practice-4c.html')).toMatch(/Practice meeting/);
 expect(read(dir+'practice-4d.html')).toMatch(/Practice checkout/);
 expect(sheet).toContain('Open the Mission 4C practice page');
});
