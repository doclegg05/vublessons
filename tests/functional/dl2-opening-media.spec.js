const {test,expect}=require('@playwright/test');
// Real media-key checks run one player at a time, as in classroom use.
test.describe.configure({mode:'default'});
const {AxeBuilder}=require('@axe-core/playwright');
const fs=require('fs'),crypto=require('crypto');
const manifest=require('../../courses/digital-literacy-2/media/manifest.json');
const base='/courses/digital-literacy-2', route=n=>`${base}/weeks/week-0${n}/presentation.html`;
const version=path=>crypto.createHash('sha256').update(fs.readFileSync(path)).digest('hex').slice(0,12);
// Netlify injects a review drawer into previews; dismiss it via its real UI before
// checking the course navigation underneath. This drawer is absent from production.
async function dismissPreviewDrawer(page){
 const host=page.locator('iframe[title="Netlify Drawer"]');
 if(!/^deploy-preview-\d+--vubcourse\.netlify\.app$/.test(new URL(page.url()).hostname))return;
 await host.waitFor({state:'attached',timeout:10000});
 const drawer=page.frameLocator('iframe[title="Netlify Drawer"]');
 const minimize=drawer.getByRole('button',{name:'Minimize',exact:true});
 const dismiss=drawer.getByRole('button',{name:'Dismiss',exact:true});
 if(!await dismiss.isVisible()){await minimize.waitFor({state:'visible',timeout:10000});await minimize.click();}
 await dismiss.click();
}
for(let week=1;week<=6;week++)test(`Week ${week}: opening, approved playback/captions, controls and return`,async({page,context})=>{
 const failures=[];page.on('pageerror',e=>failures.push(e.message));
 await page.goto(route(week)+'#1');
 if(week===1){
  await expect(page.locator('.slide.is-active')).toHaveAttribute('data-opening','pretest');
  const link=page.getByRole('link',{name:/Open the pre-test/});
  await expect(link).toHaveAttribute('target','_blank');await expect(link).toContainText('Opens a new tab');
  const popupPromise=context.waitForEvent('page');await link.click();const popup=await popupPromise;
  await popup.waitForLoadState();expect(new URL(popup.url()).pathname).toMatch(/\/assessments\/pre-test(?:\.html)?$/);
  await expect(popup.locator('body')).toContainText('20');await popup.close();
  await expect(page.locator('.strip .count')).toHaveText('1 / 28');
  await page.getByRole('button',{name:'Next: watch the video'}).click();
 }
 await expect(page.locator('.slide.is-active')).toHaveAttribute('data-opening','video');
 const video=page.locator('.slide.is-active video'),item=manifest.videos[week-1];
 await expect(video.locator('source')).toHaveAttribute('src',`/${item.path}?v=${item.sha256.slice(0,12)}`);
 await expect(video.locator('track')).toHaveAttribute('src',`/${item.captions}?v=${version(item.captions)}`);
 await expect(video).toHaveAttribute('controls','');expect(await video.getAttribute('autoplay')).toBeNull();
 await expect.poll(()=>video.evaluate(v=>v.readyState)).toBeGreaterThanOrEqual(2);
 expect(await video.evaluate(v=>v.paused)).toBe(true);
 expect(Math.abs(await video.evaluate(v=>v.duration)-item.durationSeconds)).toBeLessThan(.2);
 await expect.poll(()=>video.evaluate(v=>v.textTracks[0]?.cues?.length||0)).toBeGreaterThan(10);
 expect(await video.evaluate(v=>v.textTracks[0].mode)).toBe('showing');
 const transcript=page.getByRole('link',{name:/Transcript & chapters/});
 expect(await transcript.evaluate(a=>new URL(a.href).pathname.replace(/\.html$/,''))).toBe(`${base}/weeks/week-0${week}/video-transcript`);await expect(transcript).toHaveAttribute('target','_blank');
 // Parallel browser tests must not compete for the Mac's audible media focus.
 // The shipped player remains unmuted; only this test instance plays silently.
 expect(await video.evaluate(v=>v.muted)).toBe(false);
 await video.evaluate(v=>{v.muted=true;});
 await video.focus();await page.keyboard.press('Space');
 await expect.poll(()=>video.evaluate(v=>v.currentTime)).toBeGreaterThan(.1);
 const at=await page.evaluate(()=>DL2Deck.index());
 await page.keyboard.press('ArrowRight');await page.keyboard.press('Home');await page.keyboard.press('End');
 expect(await page.evaluate(()=>DL2Deck.index())).toBe(at);
 await video.evaluate(v=>{v.currentTime=2;return v.play();});
 await page.getByRole('button',{name:'Continue to lesson'}).click();
 await expect(page.locator('.slide.is-active')).not.toHaveAttribute('data-opening','video');
 expect(await page.locator('video').evaluate(v=>v.paused)).toBe(true);
 // Browser hash navigation, then reload and a phase jump all route through the same engine.
 await page.goto(route(week)+`#${week===1?2:1}`);await expect(page.locator('.slide.is-active video')).toBeVisible();
 await page.reload();await expect(page.locator('.slide.is-active video')).toBeVisible();
 await page.goto(route(week)+'#6');await page.goBack();await expect(page.locator('.slide.is-active video')).toBeVisible();
 await dismissPreviewDrawer(page);
 await page.locator('.strip [data-phase=present]').click();await expect(page.locator('.slide.is-active')).toHaveAttribute('data-stage','tell');
 expect(failures).toEqual([]);
});
for(const width of [1366,1920])test(`All six opening slides fit ${width} at default and enlarged sizes`,async({page})=>{
 await page.setViewportSize({width,height:width===1366?768:1080});await page.emulateMedia({reducedMotion:'reduce'});
 for(let n=1;n<=6;n++)for(const size of ['','xl','xxl']){
  await page.goto(route(n)+'#1');await page.evaluate(s=>document.documentElement.dataset.textSize=s,size);
  for(const index of n===1?[0,1]:[0]){
   await page.evaluate(i=>DL2Deck.go(i),index);
   const bad=await page.locator('.slide.is-active .panel').evaluate(panel=>{
    const b=panel.getBoundingClientRect();return [...panel.querySelectorAll('h1,p,li,video,a,button')].filter(e=>{const r=e.getBoundingClientRect();return r.width&&(r.bottom>b.bottom-3||r.top<b.top||r.right>b.right-3||r.left<b.left)}).map(e=>e.tagName+':'+e.textContent.slice(0,50));
   });expect(bad,`Week ${n}, ${size}, slide ${index+1}`).toEqual([]);
   expect(await page.evaluate(()=>document.documentElement.scrollHeight<=innerHeight&&document.documentElement.scrollWidth<=innerWidth)).toBe(true);
  }
 }
});
test('Phone openings retain visible player, large controls, links and no horizontal overflow',async({page})=>{
 await page.setViewportSize({width:390,height:844});
 for(let n=1;n<=6;n++){
  await page.goto(route(n)+'#1');await page.evaluate(()=>document.documentElement.dataset.textSize='xxl');
  if(n===1){await expect(page.getByRole('link',{name:/Open the pre-test/})).toBeVisible();await page.getByRole('button',{name:'Next: watch the video'}).click();}
  await expect(page.locator('.slide.is-active video')).toBeVisible();
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1)).toBe(true);
  expect(await page.locator('.slide.is-active .opening-guide p').evaluate(e=>parseFloat(getComputedStyle(e).fontSize))).toBeGreaterThanOrEqual(32);
  await page.getByRole('button',{name:'Continue to lesson'}).click();
 }
});
test('Old session/hash and course-home saved positions migrate once without changing assessments',async({page})=>{
 for(const [week,old,current] of [[1,0,2],[1,1,0],[1,9,10],[2,0,1],[6,22,23]]){
  await page.goto(route(week));
  const savedPath=new URL(page.url()).pathname; // local server and Netlify normalize .html differently
  await page.goto(base+'/index.html');
  await page.evaluate(({path,old})=>{sessionStorage.setItem('dl2os:slide:'+path,String(old));sessionStorage.removeItem('dl2os:slide:'+path+':version');}, {path:savedPath,old});
  await page.goto(route(week));expect(await page.evaluate(()=>DL2Deck.index())).toBe(current);
  await page.reload();expect(await page.evaluate(()=>DL2Deck.index())).toBe(current);
 }
 await page.goto(base+'/index.html');
 await page.evaluate(()=>VubProgress.saveSlide('dl2',2,8,23));await page.reload();
 await expect(page.locator('.continue-course')).toHaveAttribute('href',/#resume-23-9$/);
 await page.locator('.continue-course').click();await expect(page.locator('.strip .count')).toHaveText('10 / 36'); // Week 2 now has 36 slides (rounds and capstone, no break)
 await expect(page).not.toHaveURL(/resume-/);await page.reload();await expect(page.locator('.strip .count')).toHaveText('10 / 36');
 // Explicit opening links must win over old saved positions on a shared lab computer.
 for(const week of [1,2]){
  await page.goto(route(week)+'#1');
  await page.evaluate(()=>{const key='dl2os:slide:'+location.pathname;sessionStorage.setItem(key,'0');sessionStorage.removeItem(key+':version');});
  await page.reload();expect(await page.evaluate(()=>DL2Deck.index())).toBe(0);
 }
 // Explicit links use the current numbering; invalid/stale bounds are clamped.
 await page.goto(route(3)+'#999');await expect(page.locator('.strip .count')).toHaveText('24 / 24');
 await page.goto(route(3)+'#1');await expect(page.locator('.strip .count')).toHaveText('1 / 24');
});
test('Opening pre-test and video pass automated accessibility checks',async({page})=>{
 for(const hash of ['#1','#2']){await page.goto(route(1)+hash);const scan=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();expect(scan.violations).toEqual([]);}
});
