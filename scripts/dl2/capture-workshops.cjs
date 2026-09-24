const {chromium,expect}=require('@playwright/test');
const fs=require('fs');
const origin=process.env.DL2_REVIEW_ORIGIN||'http://localhost:3940';
(async()=>{
 const out='docs/digital-literacy-2/review/redesign';fs.mkdirSync(out,{recursive:true});const browser=await chromium.launch();
 for(const [device,width,height] of [['desktop',1440,1080],['mobile',390,844]]){
  const page=await browser.newPage({viewport:{width,height},reducedMotion:'reduce'});
  for(const [name,w,s,action] of [['opening',1,1],['calendar',1,15,'Month'],['zoom',1,5,'150%'],['sheet',3,10,'Change paper to $15'],['phishing',5,8,'Choose an independent check'],['prompt',6,7,'Build the practice prompt']]){
   await page.goto(`${origin}/courses/digital-literacy-2/weeks/week-${String(w).padStart(2,'0')}/presentation.html#slide-${s}`);
   await page.evaluate(()=>document.fonts.ready);await expect(page.locator('.deck-toolbar .vub-textsize-fab')).toBeVisible();
   const root=page.locator('.slide:not([hidden]) [data-workshop]').first();
   await page.screenshot({path:`${out}/${name}-${device}.png`,fullPage:true});
   if(action){await root.getByRole('button',{name:action,exact:true}).click();await page.screenshot({path:`${out}/${name}-${device}-changed.png`,fullPage:true});}
  }
  await page.close();
 }
 await browser.close();console.log(out);
})().catch(e=>{console.error(e);process.exit(1)});
