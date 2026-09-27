// Week 6 redesign (2026-09-26): the three practice pages behave as the lesson says, in a browser.
// Version 1 is the starter, version 2 is the agent's result with one planted defect (the typed search
// is no longer lowered, so capital letters stop matching) and version 3 is the repair.
const {test,expect}=require('@playwright/test');
const base='/courses/digital-literacy-2';

async function open(page,file){
 await page.goto(`${base}/activities/${file}`);
 const search=page.getByLabel('Search fictional'),category=page.getByLabel('Category');
 const run=async(query,cat='all')=>{await category.selectOption(cat);await search.fill(query);};
 return {run,status:page.locator('#status'),names:page.locator('#results h2')};
}
const NONE='No matching resources. Try a different word or reset the filters.';

test('Version 1 (resource-finder.html) does not search categories yet, and ignores capital letters',async({page})=>{
 const f=await open(page,'resource-finder.html');
 await f.run('LIBRARY');await expect(f.names).toHaveText(['Community library']);
 await f.run('learning');await expect(f.status).toHaveText(NONE);
 await f.run('zzz');await expect(f.status).toHaveText(NONE);
});

test('Version 2 (the agent’s result) finds categories but fails the mixed-case check',async({page})=>{
 const f=await open(page,'resource-finder-agent.html');
 await expect(page.locator('#search')).toHaveAttribute('placeholder','Try library or learning');
 await expect(page.getByText('Changed by an AI coding agent. Review and test it before you trust it.')).toBeVisible();
 await f.run('learning');await expect(f.names).toHaveText(['Community library','Practice Workbook Workshop']);await expect(f.status).toHaveText('2 fictional resources found.');
 await f.run('library');await expect(f.names).toHaveText(['Community library']);
 await f.run('zzz');await expect(f.status).toHaveText(NONE);
 // The planted defect: keep it. Version 1 finds LIBRARY; version 2 finds nothing.
 for(const query of ['LIBRARY','Learning','Library']){await f.run(query);await expect(f.status,query).toHaveText(NONE);await expect(f.names).toHaveCount(0);}
 await f.run('library','Learning');await expect(f.names).toHaveText(['Community library']);
 await f.run('library','Community');await expect(f.status).toHaveText(NONE);
});

test('Version 3 (after the repair) passes mixed case and keeps the category search',async({page})=>{
 const f=await open(page,'resource-finder-agent-fixed.html');
 await expect(page.getByText('The agent repaired the capital-letter search. Retest it before you trust it.')).toBeVisible();
 for(const query of ['LIBRARY','Library','library']){await f.run(query);await expect(f.names,query).toHaveText(['Community library']);}
 for(const query of ['Learning','learning']){await f.run(query);await expect(f.names,query).toHaveText(['Community library','Practice Workbook Workshop']);}
 await f.run('zzz');await expect(f.status).toHaveText(NONE);
 await page.getByRole('button',{name:'Reset filters'}).click();await expect(f.status).toHaveText('3 fictional resources found.');
});

for(const file of ['resource-finder.html','resource-finder-agent.html','resource-finder-agent-fixed.html'])
 test(`${file} passes the keyboard and narrow-screen checks`,async({page})=>{
  await page.goto(`${base}/activities/${file}`);
  const reached=[];
  for(let i=0;i<4;i++){await page.keyboard.press('Tab');reached.push(await page.evaluate(()=>{const a=document.activeElement;const s=getComputedStyle(a);return [a.id||a.tagName,s.outlineStyle,s.outlineWidth];}));}
  expect(reached.map(r=>r[0])).toEqual(['A','search','category','reset']);
  for(const [,style,width] of reached){expect(style).toBe('solid');expect(width).toBe('4px');}
  await page.setViewportSize({width:320,height:600});
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);
 });

test('Week 6 slide 10 shows the diff when a learner chooses what the agent changed',async({page})=>{
 await page.goto(`${base}/weeks/week-06/presentation.html`);
 await page.locator('[data-slide="9"]').click();
 const slide=page.locator('#slide-10');await expect(slide).toBeVisible();
 await slide.getByRole('button',{name:'Changed',exact:true}).click();
 const diff=slide.locator('.scene-state:visible pre');
 await expect(diff).toContainText('- const query=search.value.trim().toLowerCase();');
 await expect(diff).toContainText('+ const query=search.value.trim();');
 await expect(slide.locator('.scene-state:visible del').first()).toBeVisible();
});

test('Week 6 worksheet and answer guide fit a phone screen; the log tables scroll inside their box',async({page})=>{
 await page.setViewportSize({width:390,height:844});
 for(const f of ['worksheet.html','answer-key.html']){
  await page.goto(`${base}/weeks/week-06/${f}`);
  expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1),f).toBe(true);
 }
});

test('Week 6 worksheet test log takes typed results and prints them',async({page})=>{
 await page.goto(`${base}/weeks/week-06/worksheet.html`);
 const actual=page.getByLabel('Actual result: Mixed case');
 await actual.fill('No matching resources for LIBRARY');
 await page.emulateMedia({media:'print'});
 await expect(page.locator('#log-3-1 + .print-answer')).toHaveText('No matching resources for LIBRARY');
 await expect(actual).toBeHidden();
});
