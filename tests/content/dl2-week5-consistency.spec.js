// Week 5 (protect your work, show your skills): one scam message, current account-safety wording, and a skills
// challenge that tests what the course now teaches. Shared rebuilt-week checks are in dl2-rebuilt-weeks.spec.js.
// Source: scripts/dl2/mission-control/week5.py and scripts/dl2/curriculum.json; regenerate before running.
// DL2_ROOT points the checks at another copy of the repository (for example an export of an older commit).
const {test,expect}=require('@playwright/test');const fs=require('fs');const path=require('path');
const root=process.env.DL2_ROOT||'.';
const read=p=>fs.readFileSync(path.join(root,p),'utf8');
const dir='courses/digital-literacy-2/weeks/week-05/';
const plain=html=>html.replace(/<[^>]+>/g,' ').replace(/&amp;/g,'&').replace(/&#x27;/g,"'").replace(/&quot;/g,'"').replace(/\s+/g,' ');
const deck=plain(read(dir+'presentation.html')),sheetHtml=read(dir+'worksheet.html'),sheet=plain(sheetHtml);

test('One fictional scam message: Act now: account will close, from account-check.example',()=>{
 expect(deck).toContain('Act now: account will close');
 expect(deck).toContain('account-check.example');
 expect(deck).not.toMatch(/Act now to keep benefits/);
 expect(plain(read(dir+'practice-5b.html'))).toContain('Act now: account will close');
});

test('Account safety says two-step verification, as the test items do, never MFA',()=>{
 for(const page of [deck,sheet])expect(page).not.toMatch(/\bMFA\b/);
 expect(deck).toContain('two-step verification');
});

test('The challenge search row asks a full question and opens the organization\'s own page, as Week 2 teaches',()=>{
 expect(sheet).toMatch(/ask a better question that names the place and what you need/);
 expect(sheet).toMatch(/open the center.s own page/);
});

test('The challenge points to practice workbook data that is on the worksheet, after the challenge',()=>{
 const challenge=sheetHtml.indexOf('Five-task observation'),data=sheetHtml.indexOf('<h2>Practice workbook data</h2>');
 expect(challenge).toBeGreaterThan(-1);
 expect(data).toBeGreaterThan(challenge);
 expect(sheetHtml.slice(data)).toContain('href="/courses/digital-literacy-2/assets/supplies.csv"');
});

test('Windows 10 home updates are dated as Microsoft states them: through October 2027',()=>{
 expect(plain(read(dir+'practice-5c.html'))).toContain('until October 2027');
});

test('The skills challenge and the post-test keep their time',()=>{
 const run=plain(read(dir+'run-sheet.html'));
 expect(run).toMatch(/\(26 min\) \d+.\d+ Mission 5D/);
 expect(run).toMatch(/\(22 min\) \d+ Individual post-test/);
 expect(deck).toContain('Open the post-test');
});
