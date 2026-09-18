const {test,expect}=require('@playwright/test');
const base='/courses/digital-literacy-2';
const open=async(page,w,s)=>{await page.goto(`${base}/weeks/week-${String(w).padStart(2,'0')}/presentation.html#slide-${s}`);return page.locator('.slide:not([hidden]) [data-workshop]').first();};
test('DL2 workstation models change only the intended view and support keyboard activation',async({page})=>{
 const zoom=await open(page,1,5);const text=zoom.locator('.zoom-page p');const controls=zoom.getByRole('button',{name:'125%',exact:true});
 const before=await text.evaluate(x=>parseFloat(getComputedStyle(x).fontSize));await controls.focus();await page.keyboard.press('Enter');await expect.poll(()=>text.evaluate(x=>parseFloat(getComputedStyle(x).fontSize))).toBeGreaterThan(before);await expect(controls).toHaveAttribute('aria-pressed','true');await expect(controls).toHaveCSS('background-color','rgb(27, 54, 93)');await expect(controls).toHaveCSS('color','rgb(255, 255, 255)');
 const sound=await open(page,1,7);await sound.getByRole('button',{name:'Mute: off',exact:true}).click();await sound.getByRole('button',{name:'Run visual sound test'}).click();await expect(sound.locator('[role=status]')).toContainText('No output');await sound.getByRole('button',{name:'Mute: on',exact:true}).click();await sound.getByRole('button',{name:'Speakers',exact:true}).click();await sound.getByRole('button',{name:'Run visual sound test'}).click();await expect(sound.locator('[role=status]')).toContainText('reaches speakers');
});
test('DL2 calendar preserves events across distinct views and limits shared details',async({page})=>{
 const root=await open(page,1,15);await expect(root.getByRole('button',{name:'Week',exact:true})).toHaveAttribute('aria-pressed','true');await root.getByRole('button',{name:'Day',exact:true}).click();await expect(root.locator('.calendar-day:visible')).toHaveCount(1);await root.getByRole('button',{name:'Month',exact:true}).click();await expect(root.locator('.month-cell')).toHaveCount(28);await expect(root.locator('.month-map')).toBeVisible();await root.getByRole('button',{name:'List',exact:true}).click();await expect(root.locator('.calendar-day:visible')).toHaveCount(3);
 const privacy=await open(page,1,14);await privacy.getByRole('button',{name:'Event details',exact:true}).click();await expect(privacy.locator('[data-shared-event]')).toContainText('Room A');await privacy.getByRole('button',{name:'Free / busy',exact:true}).click();await expect(privacy.locator('[data-shared-event]')).not.toContainText('Room A');
});
test('DL2 sync deletion reaches both locations but leaves a separate recovery copy',async({page})=>{
 const root=await open(page,2,13);await root.getByRole('button',{name:'Delete synced file'}).click();await expect(root.locator('[data-local-file]')).toHaveText('File deleted');await expect(root.locator('[data-cloud-file]')).toHaveText('File deleted');await expect(root.locator('.backup-copy')).toContainText('Resource guide.docx');await root.getByRole('button',{name:'Restore from backup'}).click();await expect(root.locator('[data-cloud-file]')).toHaveText('Resource guide.docx');
});
test('DL2 spreadsheet shows referenced range and recalculates, export explains losses',async({page})=>{
 const root=await open(page,3,10);await expect(root.locator('.formula-bar')).toContainText('B5');await expect(root.locator('.formula-cell')).toHaveCount(3);await root.getByRole('button',{name:'Change paper to $15',exact:true}).click();await expect(root.locator('[data-sum]')).toHaveText('$28');await root.getByRole('button',{name:'Restore paper to $12',exact:true}).click();await expect(root.locator('[data-sum]')).toHaveText('$25');
 const out=await open(page,3,17);await out.getByRole('button',{name:'CSV',exact:true}).click();await expect(out.locator('[data-export-copy]')).toContainText('formulas are not preserved');
});
test('DL2 collaboration model turns vague feedback into an actionable change',async({page})=>{
 const root=await open(page,4,12);await root.getByRole('button',{name:'Specific suggestion',exact:true}).click();await expect(root.locator('[data-comment]')).toContainText('After step 2');await root.getByRole('button',{name:'Writer responds',exact:true}).click();await expect(root.locator('[data-comment]')).toContainText('I added the contact number');
 const meet=await open(page,4,14);await meet.getByRole('button',{name:'Raise hand',exact:true}).click();await expect(meet.locator('[role=status]')).toContainText('Wait for the host');await meet.getByRole('button',{name:'Unmute microphone',exact:true}).click();await expect(meet.locator('[data-mic-state]')).toContainText('on (model)');
});
test('DL2 safety scenarios explain independent verification and distinct protections',async({page})=>{
 const root=await open(page,5,8);await root.getByRole('button',{name:'Choose an independent check'}).click();await expect(root.locator('[role=status]')).toContainText('known official website');const protection=await open(page,5,10);await protection.getByRole('button',{name:'Read-only',exact:true}).click();await expect(protection.locator('[data-file-text]')).toContainText('Room A');await protection.getByRole('button',{name:'Encrypted',exact:true}).click();await expect(protection.locator('[data-file-text]')).not.toContainText('Room A');
 const access=await open(page,5,13);await access.getByRole('button',{name:'Deny camera',exact:true}).click();await expect(access.locator('[role=status]')).toContainText('Good fit');
});
test('DL2 app and prompt workshops handle no matches, case, blank tasks and literal input',async({page})=>{
 const app=await open(page,6,9);await app.locator('[data-resource-search]').fill('LIBRARY');await expect(app.locator('.result-row')).toHaveCount(1);await app.getByRole('button',{name:'Test no match'}).click();await expect(app.locator('.resource-results')).toContainText('No matching resources');await app.getByRole('button',{name:'Reset search'}).click();await expect(app.locator('.result-row')).toHaveCount(3);
 const prompt=await open(page,6,7);await prompt.locator('[data-prompt-task]').fill('');await prompt.getByRole('button',{name:'Build the practice prompt'}).click();await expect(prompt.locator('[data-prompt-task]')).toBeFocused();await prompt.locator('[data-prompt-task]').fill('<img src=x onerror=alert(1)>');await prompt.getByRole('button',{name:'Build the practice prompt'}).click();await expect(prompt.locator('[data-prompt-output]')).toContainText('<img');await expect(prompt.locator('[data-prompt-output] img')).toHaveCount(0);await expect(prompt.locator('[data-prompt-output]')).toContainText('Support keyboard access');
});
test('DL2 mobile workshop keeps text controls in flow and model instructions at classroom size',async({page})=>{
 await page.setViewportSize({width:390,height:844});
 for(const [w,s] of [[1,1],[1,15],[3,10],[5,8],[6,7]]){
  const root=await open(page,w,s);await expect(page.locator('.deck-toolbar .vub-textsize-fab')).toBeVisible();expect(await page.locator('.vub-textsize-fab').evaluate(x=>getComputedStyle(x).position)).toBe('static');expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBeTruthy();
  if(w===1&&s===15){const calendar=root.locator('.calendar-surface');await calendar.focus();await page.keyboard.press('ArrowRight');expect(await calendar.evaluate(x=>x.scrollLeft)).toBeGreaterThan(0);await expect(page).toHaveURL(/#slide-15$/);}
  for(const el of await root.locator('.calendar-event span,.prompt-preview,.demo-sheet td,.formula-bar code').all())expect(await el.evaluate(x=>parseFloat(getComputedStyle(x).fontSize))).toBeGreaterThanOrEqual(32);
 }
});
test('DL2 workshop initial and changed states meet automated WCAG A/AA checks',async({page})=>{
 const AxeBuilder=require('@axe-core/playwright').default;
 for(const [w,s,action] of [[1,5,'150%'],[1,15,'Month'],[3,10,'Change paper to $15'],[4,12,'Specific suggestion'],[5,8,'Choose an independent check'],[6,7,'Build the practice prompt']]){
  const root=await open(page,w,s);
  for(const changed of [false,true]){
   if(changed)await root.getByRole('button',{name:action,exact:true}).click();
   const results=await new AxeBuilder({page}).include('.slide:not([hidden])').withTags(['wcag2a','wcag2aa','wcag21a','wcag21aa']).analyze();
   expect(results.violations,`Week ${w}, slide ${s}, changed=${changed}`).toEqual([]);
  }
 }
});
