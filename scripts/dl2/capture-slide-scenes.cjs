const {chromium}=require(process.cwd()+'/node_modules/@playwright/test');
const fs=require('fs');
(async()=>{const b=await chromium.launch();const out='docs/digital-literacy-2/review/slide-scenes';fs.mkdirSync(out,{recursive:true});
for(const [device,width,height] of [['desktop',1440,1080],['mobile',390,844]]){
 const p=await b.newPage({viewport:{width,height},reducedMotion:'reduce'});
 for(const [name,week,slide,choice] of [['chart',3,11,'changed'],['crop',3,13,'crop'],['trim',3,14,'split'],['storage',6,13,'2'],['email',4,5,'2'],['search',2,3,'2'],['workstation',1,9,'1'],['safety',5,2,null]]){
 await p.goto(`http://localhost:3940/courses/digital-literacy-2/weeks/week-0${week}/presentation.html#slide-${slide}`);await p.evaluate(()=>document.fonts.ready);
 if(choice)await p.locator(`#slide-${slide} [data-scene-choice="${choice}"],#slide-${slide} [data-chart="${choice}"],#slide-${slide} [data-crop="${choice}"],#slide-${slide} [data-trim="${choice}"]`).click();
 await p.screenshot({path:`${out}/${name}-${device}.png`,fullPage:true});
 }
 await p.close();
}await b.close();})();
