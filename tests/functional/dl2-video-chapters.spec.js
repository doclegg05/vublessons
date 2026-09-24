const {test,expect}=require('@playwright/test');
const fs=require('fs');
const base='/courses/digital-literacy-2';
test('DL2 teaching videos expose ten accurate, keyboard-operated chapters without autoplay',async({page})=>{
 for(let n=1;n<=6;n++){
  const week=`week-${String(n).padStart(2,'0')}`;
  const beats=JSON.parse(fs.readFileSync(`video/digital-literacy-2/${week}/narration/beats.json`));
  await page.goto(`${base}/weeks/${week}/video-transcript.html`);
  const video=page.locator('video');await page.locator('.video-chapters summary').click();
  const controls=page.locator('[data-video-seek]');await expect(controls).toHaveCount(10);
  await expect(page.locator('#transcript-content section')).toHaveCount(10);
  for(const i of [0,4,9]){
   const control=controls.nth(i);await control.focus();await page.keyboard.press('Enter');
   await expect.poll(()=>video.evaluate(v=>v.currentTime)).toBeCloseTo(beats[i].start,1);
   expect(await video.evaluate(v=>v.paused)).toBe(true);await expect(video).toBeFocused();
   await expect(control).toHaveAttribute('aria-current','true');
   await expect(page.locator('#transcript-content section').nth(i)).toContainText(beats[i].text);
  }
 }
});
test('DL2 lesson and transcript chapters fit enlarged mobile text and retain native video keys',async({page})=>{
 await page.setViewportSize({width:390,height:844});
 for(const route of ['presentation','video-transcript']){
  await page.goto(`${base}/weeks/week-01/${route}.html`);
  if(route==='presentation'){
   await page.getByRole('button',{name:'Show lesson navigation'}).click();
   await page.locator('[data-slide]').filter({hasText:/Watch:/}).click();
  }
  await page.evaluate(()=>document.documentElement.setAttribute('data-text-size','xxl'));
  await page.locator('.video-chapters summary').click();
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);
  expect(await page.locator('[data-video-seek]').evaluateAll(buttons=>buttons.every(b=>b.getBoundingClientRect().right<=innerWidth&&b.scrollWidth<=b.clientWidth+1))).toBe(true);
  await page.locator('[data-video-seek]').last().click();
  const active=route==='presentation'?await page.locator('.slide:not([hidden])').getAttribute('id'):null;
  await page.keyboard.press('ArrowLeft');
  if(active)expect(await page.locator('.slide:not([hidden])').getAttribute('id')).toBe(active);
  expect(await page.locator('video').evaluate(v=>v.paused)).toBe(true);
 }
});
test('DL2 screen demonstrations are replayable and the app exercise matches the narrated checks',async({page})=>{
 for(let n=1;n<=6;n++){
  await page.goto(`${base}/weeks/week-${String(n).padStart(2,'0')}/video-transcript.html`);
  await page.locator('.video-chapters summary').click();
  const demos=page.getByRole('button',{name:/Screen demo/});
  await expect(demos).toHaveCount(2);
  await expect(page.locator('.screen-demo-guide')).toHaveCount(2);
  await demos.first().focus();await page.keyboard.press('Enter');
  await expect(page.locator('video')).toBeFocused();
  expect(await page.locator('video').evaluate(v=>v.paused)).toBe(true);
  // Cues in walkthroughs use the title band, away from fields and results.
  await expect.poll(()=>page.locator('video').evaluate(v=>v.textTracks[0]?.cues?.length||0)).toBeGreaterThan(0);
  expect(await page.locator('video').evaluate(v=>[...v.textTracks[0].cues].filter(c=>c.startTime>=v.currentTime-.01&&c.startTime<v.currentTime+10).every(c=>c.line===0))).toBe(true);
  for(const guide of await page.locator('.screen-demo-guide').all()){
   await guide.locator('summary').click();
   await expect(guide).toContainText('fictional practice data');
   expect(await guide.locator('li').count()).toBeGreaterThanOrEqual(5);
  }
 }
 await page.goto(`${base}/activities/resource-finder.html`);
 const search=page.getByLabel('Search fictional');
 for(const query of ['library','LIBRARY']){
  await search.fill(query);
  await expect(page.locator('#results h2')).toHaveText('Community library');
 }
 await search.fill('zzz');await expect(page.locator('#status')).toContainText('No matching resources');
 await search.fill('LIBRARY');await page.getByLabel('Category').selectOption('Learning');
 await expect(page.locator('#results h2')).toHaveText('Community library');
 await page.getByLabel('Category').selectOption('Community');
 await expect(page.locator('#results h2')).toHaveCount(0);
 await expect(page.locator('#status')).toContainText('No matching resources');
});
