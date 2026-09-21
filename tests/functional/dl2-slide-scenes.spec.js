const {test,expect}=require('@playwright/test');
const AxeBuilder=require('@axe-core/playwright').default;
const base='/courses/digital-literacy-2/weeks';
for(let week=1;week<=6;week++)test(`DL2 week ${week}: illustrated teaching choices work with keyboard and enlarged mobile text`,async({page})=>{
 await page.goto(`${base}/week-0${week}/presentation.html`);
 const ids=await page.locator('.slide:has([data-topic-scene])').evaluateAll(slides=>slides.map(s=>s.id));
 expect(ids.length).toBeGreaterThan(4);
 for(const id of ids){
  await page.locator(`[data-slide="${Number(id.split('-')[1])-1}"]`).click();
  for(const scene of await page.locator(`#${id} [data-topic-scene]`).all()){
   const first=await scene.locator('.scene-state:visible').innerText();
   const last=scene.locator('[data-scene-choice]').last();await last.focus();await page.keyboard.press('Space');
   await expect(last).toHaveAttribute('aria-pressed','true');await expect(scene.locator('.scene-state:visible')).toHaveCount(1);
   expect(await scene.locator('.scene-state:visible').innerText()).not.toBe(first);
   await expect(page).toHaveURL(new RegExp(`#${id}$`));
  }
  for(const img of await page.locator(`#${id} img:visible`).all()){
   await img.scrollIntoViewIfNeeded();await expect.poll(()=>img.evaluate(i=>i.complete&&i.naturalWidth>0)).toBeTruthy();
  }
 }
 const axe=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();expect(axe.violations.map(v=>({id:v.id,nodes:v.nodes.map(n=>n.target)}))).toEqual([]);
 await page.setViewportSize({width:390,height:844});
 for(let n=0;n<3;n++)await page.getByRole('button',{name:'Increase text size'}).click();
 for(const id of ids){
  await page.evaluate(id=>{location.hash=id},id);await expect(page.locator(`#${id}`)).toBeVisible();
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),id).toBeTruthy();
 }
});
test('DL2 chart keeps bars, labels, order and data table aligned',async({page})=>{
 await page.goto(`${base}/week-03/presentation.html#slide-11`);
 const lab=page.locator('[data-chart-lab]');
 await lab.getByRole('button',{name:'Paper becomes $15',exact:true}).click();
 await expect(lab.locator('[data-chart-paper]')).toHaveText('15');await expect(lab.locator('[data-item="Paper"] b')).toHaveText('$15');
 await expect(lab.locator('.bar-chart')).toHaveAttribute('aria-label',/Paper 15 dollars/);
 await lab.getByRole('button',{name:'Lowest cost first',exact:true}).click();
 await expect(lab.locator('.bar-row').first()).toHaveAttribute('data-item','Pens');await expect(lab.locator('[data-chart-paper]')).toHaveText('12');
 await lab.getByRole('button',{name:'Compare costs',exact:true}).click();await expect(lab.locator('.bar-row').first()).toHaveAttribute('data-item','Paper');
 await expect(lab.locator('[data-chart-paper]')).toHaveText('12');
 const axe=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();expect(axe.violations).toEqual([]);
});
test('DL2 crop and resize demonstrate distinct reversible edits',async({page})=>{
 await page.goto(`${base}/week-03/presentation.html#slide-13`);await page.emulateMedia({reducedMotion:'reduce'});
 const lab=page.locator('[data-crop-lab]');const frame=lab.locator('.image-edit-frame');const original=(await frame.boundingBox()).width;
 await lab.getByRole('button',{name:'Crop the edges',exact:true}).click();await expect(frame).toHaveCSS('clip-path','inset(15% 18%)');expect((await frame.boundingBox()).width).toBe(original);
 await lab.getByRole('button',{name:'Resize proportionally',exact:true}).click();await expect(frame).toHaveCSS('clip-path','none');expect((await frame.boundingBox()).width).toBeLessThan(original);
 await lab.getByRole('button',{name:'Original',exact:true}).click();expect((await frame.boundingBox()).width).toBe(original);
 const axe=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();expect(axe.violations).toEqual([]);
});
test('DL2 editing timeline distinguishes trimming ends from removing a middle section',async({page})=>{
 await page.goto(`${base}/week-03/presentation.html#slide-14`);const lab=page.locator('[data-trim-lab]');
 await lab.getByRole('button',{name:'Trim the start and end'}).click();await expect(lab.locator('.clip-removed')).toHaveCount(2);await expect(lab.locator('[data-trim-note]')).toContainText('14 seconds');
 await lab.getByRole('button',{name:'Remove a middle section'}).click();await expect(lab.locator('.clip-removed')).toHaveCount(1);await expect(lab.locator('[data-clip="middle"]')).toHaveClass(/clip-removed/);await expect(lab.locator('[data-trim-note]')).toContainText('17 seconds');
 await lab.getByRole('button',{name:'Original clip'}).click();await expect(lab.locator('.clip-removed')).toHaveCount(0);
 const axe=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();expect(axe.violations).toEqual([]);
});
test('DL2 practice steps toggle without moving the lesson; print retains teaching explanations',async({page})=>{
 await page.goto(`${base}/week-01/presentation.html#slide-4`);const step=page.locator('#slide-4 [data-step-done]').first();
 await step.focus();await page.keyboard.press('Enter');await expect(step).toHaveAttribute('aria-pressed','true');await expect(step).toContainText('Practiced');await expect(page).toHaveURL(/#slide-4$/);await step.click();await expect(step).toHaveAttribute('aria-pressed','false');
 await page.emulateMedia({media:'print'});await expect(page.locator('#slide-8 .scene-state')).toHaveCount(3);
 for(const panel of await page.locator('#slide-8 .scene-state').all())await expect(panel).toBeVisible();
});

test('DL2 email draft reviews recipient, subject and attachment without sending',async({page})=>{
 await page.goto(`${base}/week-04/presentation.html#slide-4`);
 const scene=page.locator('#slide-4 [data-topic-scene]');
 await expect(scene).toContainText('Build an actionable email draft');
 await expect(scene.locator('.scene-state:visible')).toContainText('Alex');
 await scene.getByRole('button',{name:'Subject',exact:true}).focus();await page.keyboard.press('Enter');
 await expect(scene.locator('.scene-state:visible .visual-selected')).toContainText('Review the computer-help handout');
 await scene.getByRole('button',{name:'Attachment',exact:true}).click();
 await expect(scene.locator('.scene-state:visible .visual-selected')).toContainText('computer-help-handout-v1.docx');
 await expect(page.locator('#slide-4 [data-workshop="feedback"]')).toHaveCount(0);
 await expect(scene.getByRole('button',{name:'Send',exact:true})).toHaveCount(0);
});
test('DL2 recovery distinguishes missing file from wrong content before restoration',async({page})=>{
 await page.goto(`${base}/week-02/presentation.html#slide-18`);
 const scene=page.locator('#slide-18 [data-topic-scene]');
 await expect(scene.locator('.scene-state:visible')).toContainText('Trash preview');
 await scene.getByRole('button',{name:'Wrong content',exact:true}).click();
 await expect(scene.locator('.scene-state:visible')).toContainText('Version history');
 await expect(scene.locator('.scene-state:visible')).toContainText('Coordinate with collaborators');
 await scene.getByRole('button',{name:'Restore checked copy',exact:true}).click();
 await expect(scene.locator('.scene-state:visible')).toContainText('Open and check useful content');
 await scene.getByRole('button',{name:'Missing file',exact:true}).click();
 await expect(scene.locator('.scene-state:visible')).toContainText('Deleted');
});
test('DL2 live supply input and illustrated worksheet stay synchronized including zero',async({page})=>{
 await page.goto(`${base}/week-03/presentation.html#slide-9`);
 const input=page.locator('#paper-cost');
 for(const [value,total] of [['15','28.00'],['0','13.00'],['12','25.00']]){
  await input.fill(value);
  await expect(page.locator('#budget-total')).toHaveText(`Total: $${total}`);
  await expect(page.locator('[data-budget-paper]')).toHaveText(Number(value).toFixed(2));
  await expect(page.locator('[data-budget-sum]')).toHaveText(total);
 }
 await input.fill('');
 await expect(page.locator('#budget-total')).toHaveText('Enter a nonnegative paper cost.');
 await expect(page.locator('[data-budget-paper]')).toHaveText('—');
 await expect(page.locator('[data-budget-sum]')).toHaveText('—');
});
