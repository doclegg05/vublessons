// Mission Control extension: legacy simulation checks now exercise the retained practice library.
const {test,expect}=require('@playwright/test');
const base='/courses/digital-literacy-2';
const open=async(page,w,s)=>{await page.goto(`${base}/weeks/week-${String(w).padStart(2,'0')}/practice.html#slide-${s}`);return page.locator('.slide:not([hidden]) [data-workshop]').first();};
// Restored 2026-09-28 (final review). These two drove workshops on the replaced week 1 deck (display zoom, sound output,
// calendar views, shared-calendar privacy), which no live week has now. The shared assets/workshop.js behaviors they
// checked are still used on weeks 3-5, so they are retargeted there: keyboard-activated choice buttons that change only
// their own view and show the pressed state, toggle buttons that say their state in words, view switches that keep the
// content, and a protection choice that hides details.
test('DL2 workstation models change only the intended view and support keyboard activation',async({page})=>{
 const doc=await open(page,3,3);const page3=doc.locator('[data-document]');const outline=page.locator('#slide-3 .authored-window');
 const outlineBefore=await outline.innerHTML();
 const structured=doc.getByRole('button',{name:'Heading + steps',exact:true});
 await expect(doc.getByRole('button',{name:'Plain paragraphs',exact:true})).toHaveAttribute('aria-pressed','true');await expect(page3).not.toHaveClass(/structured/);
 await structured.focus();await page.keyboard.press('Enter');
 await expect(page3).toHaveClass(/structured/);await expect(structured).toHaveAttribute('aria-pressed','true');await expect(doc.getByRole('button',{name:'Plain paragraphs',exact:true})).toHaveAttribute('aria-pressed','false');
 await expect(structured).toHaveCSS('background-color','rgb(27, 54, 93)');await expect(structured).toHaveCSS('color','rgb(255, 255, 255)');
 expect(await outline.innerHTML(),'the rest of the slide is unchanged').toBe(outlineBefore);
 const meeting=await open(page,4,14);const mic=meeting.getByRole('button',{name:'Unmute microphone',exact:true});
 await mic.click();await expect(meeting.getByRole('button',{name:'Mute microphone',exact:true})).toHaveAttribute('aria-pressed','true');
 await expect(meeting.locator('[data-mic-state]')).toHaveText('Microphone on (model)');await expect(meeting.locator('[role=status]')).toContainText('microphone is on');
 await meeting.getByRole('button',{name:'Mute microphone',exact:true}).click();await expect(meeting.locator('[data-mic-state]')).toHaveText('Microphone muted');await expect(meeting.locator('[role=status]')).toContainText('is muted');
 await meeting.getByRole('button',{name:'Raise hand',exact:true}).click();await expect(meeting.getByRole('button',{name:'Lower hand',exact:true})).toHaveAttribute('aria-pressed','true');
 await expect(meeting.locator('[data-mic-state]'),'raising a hand leaves the microphone alone').toHaveText('Microphone muted');
});
test('DL2 workshop views keep their content across switches and a protection choice limits shared details',async({page})=>{
 const exp=await open(page,3,17);await expect(exp.getByRole('button',{name:'Editable document',exact:true})).toHaveAttribute('aria-pressed','true');
 await exp.getByRole('button',{name:'PDF',exact:true}).click();await expect(exp.locator('[data-extension]')).toHaveText('PDF');
 await exp.getByRole('button',{name:'CSV',exact:true}).click();await expect(exp.locator('[data-extension]')).toHaveText('CSV');await expect(exp.locator('[data-export-copy]')).toContainText('Formatting and formulas are not preserved');
 await exp.getByRole('button',{name:'Editable document',exact:true}).click();await expect(exp.locator('[data-extension]')).toHaveText('DOCX');await expect(exp.locator('[data-export-title]')).toHaveText('Keep revising together');
 const enc=await open(page,5,10);const file=enc.locator('[data-file-text]');
 await expect(enc.getByRole('button',{name:'Original data',exact:true})).toHaveAttribute('aria-pressed','true');await expect(file).toContainText('Room A');
 await enc.getByRole('button',{name:'Encrypted',exact:true}).click();await expect(file).not.toContainText('Room A');await expect(enc.locator('[data-protection]')).toHaveText('Encrypted file');
 await enc.getByRole('button',{name:'Read-only',exact:true}).click();await expect(file).toContainText('Room A');await expect(enc.locator('[data-protection]')).toHaveText('Read-only file');
});
test('DL2 sync deletion reaches both locations but leaves a separate recovery copy',async({page})=>{
 const root=await open(page,2,13);await root.getByRole('button',{name:'Delete synced file'}).click();await expect(root.locator('[data-local-file]')).toHaveText('File deleted');await expect(root.locator('[data-cloud-file]')).toHaveText('File deleted');await expect(root.locator('.backup-copy')).toContainText('library-help-v1.docx');await root.getByRole('button',{name:'Restore from backup'}).click();await expect(root.locator('[data-cloud-file]')).toHaveText('library-help-v1.docx');
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
 const prompt=await open(page,6,7);await prompt.locator('[data-prompt-task]').fill('');await prompt.getByRole('button',{name:'Build the practice prompt'}).click();await expect(prompt.locator('[data-prompt-task]')).toBeFocused();await prompt.locator('[data-prompt-task]').fill('<img src=x onerror=alert(1)>');await prompt.getByRole('button',{name:'Build the practice prompt'}).click();await expect(prompt.locator('[data-prompt-output]')).toContainText('<img');await expect(prompt.locator('[data-prompt-output] img')).toHaveCount(0);await expect(prompt.locator('[data-prompt-output]')).toContainText('Keep keyboard use and the visible outline.');await expect(prompt.locator('[data-prompt-output]')).toContainText('Show me your plan before you change anything');
});
// Narrowed 2026-09-28 (Mission Control, Task 11): week 1 slides 1 and 15 (and the calendar-scroll check that only
// applied to week 1 slide 15) dropped with the replaced deck; weeks 3, 5 and 6 unchanged.
test('DL2 mobile workshop keeps text controls in flow and model instructions at classroom size',async({page})=>{
 await page.setViewportSize({width:390,height:844});
 for(const [w,s] of [[3,10],[5,8],[6,7]]){
  const root=await open(page,w,s);await expect(page.locator('.deck-toolbar .vub-textsize-fab')).toBeVisible();expect(await page.locator('.vub-textsize-fab').evaluate(x=>getComputedStyle(x).position)).toBe('static');expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBeTruthy();
  for(const el of await root.locator('.calendar-event span,.prompt-preview,.demo-sheet td,.formula-bar code').all())expect(await el.evaluate(x=>parseFloat(getComputedStyle(x).fontSize))).toBeGreaterThanOrEqual(32);
 }
});
// Narrowed 2026-09-28 (Mission Control, Task 11): week 1 slides 5 and 15 dropped with the replaced deck.
test('DL2 workshop initial and changed states meet automated WCAG A/AA checks',async({page})=>{
 const AxeBuilder=require('@axe-core/playwright').default;
 for(const [w,s,action] of [[3,10,'Change paper to $15'],[4,12,'Specific suggestion'],[5,8,'Choose an independent check'],[6,7,'Build the practice prompt']]){
  const root=await open(page,w,s);
  for(const changed of [false,true]){
   if(changed)await root.getByRole('button',{name:action,exact:true}).click();
   const results=await new AxeBuilder({page}).include('.slide:not([hidden])').withTags(['wcag2a','wcag2aa','wcag21a','wcag21aa']).analyze();
   expect(results.violations,`Week ${w}, slide ${s}, changed=${changed}`).toEqual([]);
  }
 }
});
