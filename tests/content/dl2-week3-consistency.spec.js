// Week 3 (resource pack): facts the deck, the worksheet, the practice page and the video must share.
// Checks every rebuilt week shares (no break, practice pages, Show pictures, round labels) are in dl2-rebuilt-weeks.spec.js.
// Source: scripts/dl2/mission-control/week3.py, visuals.py and build.py; regenerate before running.
// DL2_ROOT points the checks at another copy of the repository (for example an export of an older commit).
const {test,expect}=require('@playwright/test');const fs=require('fs');const path=require('path');
const root=process.env.DL2_ROOT||'.';
const read=p=>fs.readFileSync(path.join(root,p),'utf8');
const dir='courses/digital-literacy-2/weeks/week-03/';
const slides=read(dir+'presentation.html').split('<section class="slide').slice(1);
const sheet=read(dir+'worksheet.html');
const heading=slide=>slide.match(/<h1[^>]*>(.*?)<\/h1>/)[1];
const plain=html=>html.replace(/<[^>]+>/g,' ').replace(/&amp;/g,'&').replace(/&#x27;/g,"'").replace(/\s+/g,' ');

test('Supplies are listed in the CSV order everywhere: paper, folders, pens',()=>{
 const csv=read('courses/digital-literacy-2/assets/supplies.csv').split('\n').slice(1,4).map(r=>r.split(',')[0]);
 expect(csv).toEqual(['Paper','Folders','Pens']);
 const deck=plain(slides.join(' ')).toLowerCase();
 expect(deck).toContain('paper $12 + folders $8 + pens $5');
 expect(deck).not.toMatch(/pens \$8|pens \+ folders/);
});

test('Clip editing has its own practice page, linked from its round on the slide and the worksheet',()=>{
 const round=slides.find(s=>heading(s)==='Round 4: Trim and split a clip');
 expect(round).toContain('href="practice-3d.html" target="_blank"');
 expect(sheet.match(/id="m3D-r4".*?<\/h3><p class="app-line">(.*?)<\/p>/s)[1]).toContain('href="practice-3d.html"');
 expect(read(dir+'practice-3d.html')).toContain('data-trim-lab');
});
