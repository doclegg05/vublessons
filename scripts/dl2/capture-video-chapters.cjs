const {chromium}=require('playwright');
const AxeBuilder=require('@axe-core/playwright').default;
const fs=require('fs');
(async()=>{
 const browser=await chromium.launch();
 const context=await browser.newContext();
 const page=await context.newPage();
 const out='docs/digital-literacy-2/review/video-teaching';
 const base=process.env.DL2_REVIEW_BASE_URL||'http://localhost:3939';
 const report=[];
 fs.mkdirSync(out,{recursive:true});
 for(const [name,width] of [['desktop',1440],['mobile',390]]){
  await page.setViewportSize({width,height:900});
  await page.goto(`${base}/courses/digital-literacy-2/weeks/week-01/video-transcript.html`);
  if(width<500)await page.evaluate(()=>document.documentElement.setAttribute('data-text-size','xxl'));
  await page.locator('.video-chapters summary').click();
  await page.locator('[data-video-seek]').nth(4).click();
  await page.locator('.video-chapters').screenshot({path:`${out}/chapters-${name}.png`});
  const result=await new AxeBuilder({page}).include('.video-chapters').withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();
  report.push({viewport:name,violations:result.violations.map(v=>({id:v.id,impact:v.impact}))});
 }
 fs.writeFileSync(`${out}/chapter-accessibility.json`,JSON.stringify(report,null,2)+'\n');
 console.log(report);
 await browser.close();
 if(report.some(r=>r.violations.length))process.exitCode=1;
})();
