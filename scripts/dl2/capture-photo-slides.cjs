const {chromium}=require(process.cwd()+'/node_modules/@playwright/test');
const fs=require('fs');
(async()=>{
 const browser=await chromium.launch();const out='docs/digital-literacy-2/review/photo-slides';fs.mkdirSync(out,{recursive:true});
 const measurements=[];
 for(const [device,width,height] of [['desktop',1440,1080],['mobile',390,844]]){
  const p=await browser.newPage({viewport:{width,height},reducedMotion:'reduce'});
  for(const [week,slide,name] of [[1,12,'print'],[2,18,'recovery'],[3,12,'storyboard'],[4,4,'email'],[5,1,'safety'],[5,3,'comfort'],[6,13,'data-boundaries']]){
   await p.goto(`http://localhost:3939/courses/digital-literacy-2/weeks/week-0${week}/presentation.html#slide-${slide}`);
   await p.evaluate(()=>document.fonts.ready);
   await p.locator(`#slide-${slide}`).screenshot({path:`${out}/${name}-${device}.png`});
   measurements.push({name,device,overflow:await p.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1),slideHeight:(await p.locator(`#slide-${slide}`).boundingBox()).height});
  }
  await p.close();
 }
 fs.writeFileSync(`${out}/measurements.json`,JSON.stringify(measurements,null,2));await browser.close();
})();
