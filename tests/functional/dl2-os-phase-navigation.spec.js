const { test, expect } = require('@playwright/test');
const URL = '/courses/digital-literacy-2/weeks/week-01/presentation.html';
const phases = [
  ['warm-up', 'Warm-up', 3], ['intro', 'Intro', 4], ['present', 'Present', 5],
  ['practice', 'Practice', 7], ['evaluate', 'Evaluate', 8], ['apply', 'Apply', 26]
];
const button = (page, id) => page.locator(`.strip button[data-phase="${id}"]`);
async function verify(page, id, slide) {
  await expect(page.locator('.slide.is-active')).toHaveAttribute('data-phase', id);
  await expect(page.locator('.strip .count')).toHaveText(`${slide} / 27`);
  await expect(page).toHaveURL(new RegExp(`#${slide}$`));
  await expect(button(page, id)).toHaveAttribute('aria-current', 'step');
  await expect(page.locator('.strip [aria-current="step"]')).toHaveCount(1);
  await expect(page.locator('.slide.is-active')).toHaveAttribute('data-step', '0');
  await expect.poll(() => page.evaluate(() => {
    const progress = JSON.parse(localStorage.getItem('vub:progress:v1') || '{}');
    return progress.dl2?.['1']?.slide;
  })).toBe(slide - 1);
  expect(await page.evaluate(() => sessionStorage.getItem('dl2os:slide:' + location.pathname))).toBe(String(slide - 1));
}
for (const vp of [{width:1366,height:768},{width:1920,height:1080}]) {
  test(`phase buttons jump forward and backward without overflow at ${vp.width}x${vp.height}`, async ({page}) => {
    await page.setViewportSize(vp);
    await page.emulateMedia({reducedMotion:'reduce'});
    await page.goto(URL+'#1');
    await expect(page.locator('.strip button[data-phase]')).toHaveCount(6);
    for (const [id,label,slide] of [...phases,...phases.slice().reverse()]) {
      await expect(button(page,id)).toHaveAccessibleName(`${label}: jump to slide ${slide}`);
      await button(page,id).click();
      await verify(page,id,slide);
      expect(await button(page,id).evaluate(e => {
        const r=e.getBoundingClientRect();
        return r.left>=0 && r.top>=0 && r.right<=innerWidth+1 && r.bottom<=innerHeight+1 && e.scrollWidth<=e.clientWidth+1;
      })).toBe(true);
      expect(await page.evaluate(() => document.documentElement.scrollHeight<=innerHeight && document.documentElement.scrollWidth<=innerWidth)).toBe(true);
    }
    await button(page,'apply').click();await page.reload();await verify(page,'apply',26);
  });
}
test('all six phase buttons support Enter and Space, visible focus, and build reset',async ({page})=>{
  await page.goto(URL+'#1');
  for(const key of ['Enter','Space'])for(const [id,,slide]of phases){
    await button(page,id).focus();
    await expect(button(page,id)).toHaveCSS('outline-style','solid');
    await page.keyboard.press(key);await verify(page,id,slide);
    await expect(button(page,id)).toBeFocused();
  }
  await button(page,'warm-up').click();await page.keyboard.press('ArrowRight');
  await expect(page.locator('.slide.is-active .build.on')).toHaveCount(1);
  await button(page,'warm-up').click();await expect(page.locator('.slide.is-active .build.on')).toHaveCount(0);
  await button(page,'present').click();
  await page.keyboard.press('6');await page.keyboard.press('Enter'); // existing numeric jump to Show A
  await page.keyboard.press('ArrowRight'); // existing demo step
  await button(page,'apply').click();await button(page,'present').click();
  await verify(page,'present',5);
  await page.keyboard.press('6');await page.keyboard.press('Enter');
  await expect(page.locator('.slide.is-active .demo-cap')).toBeVisible();
});
test('phase jump clears a pending numeric jump and remains usable in full screen',async ({page})=>{
  await page.goto(URL+'#1');
  await page.keyboard.press('2');await button(page,'apply').click();
  await button(page,'warm-up').focus();await page.keyboard.press('Enter');await verify(page,'warm-up',3);
  await page.keyboard.press('f');
  await expect.poll(()=>page.evaluate(()=>!!document.fullscreenElement)).toBe(true);
  for(const [id,,slide]of phases){await button(page,id).click();await verify(page,id,slide);}
  await page.keyboard.press('f');await expect.poll(()=>page.evaluate(()=>!!document.fullscreenElement)).toBe(false);
});
