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
