// Seek every instructional state and verify its visible, readable result.
import {chromium} from '@playwright/test';
import fs from 'node:fs/promises';
import path from 'node:path';
const root=process.cwd();
const browser=await chromium.launch({headless:true});
const page=await browser.newPage({viewport:{width:1280,height:720},deviceScaleFactor:1});
const errors=[]; const checks=[];
page.on('pageerror', e=>errors.push(e.message));
const out=path.join(root,'video/digital-literacy-2/screen-share-review');
await fs.mkdir(out,{recursive:true});
const font=await fs.readFile(path.join(root,'assets/fonts/source-sans-3-latin-400-normal.woff2'));
const bold=await fs.readFile(path.join(root,'assets/fonts/source-sans-3-latin-700-normal.woff2'));
for(let n=1;n<=6;n++){
 const week=`week-${String(n).padStart(2,'0')}`;
 const dir=path.join(root,'video/digital-literacy-2',week);
 const scenes=JSON.parse(await fs.readFile(path.join(dir,'screen-share-actions.json')));
 for(const scene of scenes){
  const cid=`w${n}-scene-${scene.chapter}`;
  const markup=(await fs.readFile(path.join(dir,`compositions/frames/scene-${scene.chapter}.html`),'utf8')).replace('<template>','').replace('</template>','');
  await page.setContent(`<style>@font-face{font-family:VUB;src:url(data:font/woff2;base64,${font.toString('base64')})}@font-face{font-family:VUB;font-weight:700;src:url(data:font/woff2;base64,${bold.toString('base64')})}*{box-sizing:border-box}body{margin:0;width:1280px;height:720px}</style>`);
  await page.addScriptTag({path:path.join(root,'video/digital-literacy-2/production/node_modules/gsap/dist/gsap.min.js')});
  await page.evaluate(()=>{window.__timelines={};});
  await page.evaluate(html=>{const div=document.createElement('div');div.innerHTML=html;document.body.append(div);for(const old of div.querySelectorAll('script')){const script=document.createElement('script');script.textContent=`(()=>{${old.textContent}})()`;old.replaceWith(script);}},markup);
  await page.evaluate(()=>document.fonts.ready);
  // Reverse seeking checks deterministic rendering too, not only forward playback.
  for(const j of [...scene.actions.keys()].reverse()){
   const action=scene.actions[j]; const at=action.at+Math.min(.7,((scene.actions[j+1]?.at??scene.durationSeconds)-action.at)/2);
   const result=await page.evaluate(({cid,at,j})=>{
    window.__timelines[cid].seek(at,false);
    const visible=[...document.querySelectorAll('.screen-state')].filter(e=>Number(getComputedStyle(e).opacity)>.99);
    const bounds=[];
    for(const el of [...(visible[0]?.querySelectorAll('text')??[]),document.querySelector('.action-label')]){
     const r=el.getBoundingClientRect();
     if(r.left<38||r.right>1242||r.top<100||r.bottom>653) bounds.push({text:el.textContent,x:r.x,y:r.y,right:r.right,bottom:r.bottom});
    }
    return {state:visible.map(e=>e.id),label:document.querySelector('.action-label').textContent,bounds,text:visible[0]?.textContent};
   },{cid,at,j});
   if(result.state.length!==1||result.state[0]!==`${cid}-state-${j}`||result.label!==action.label||result.bounds.length) errors.push({week,chapter:scene.chapter,action:j,at,...result});
   const screenshot=`${week}-chapter-${scene.chapter}-state-${j}.png`;
   checks.push({week,chapter:scene.chapter,action:j,at,globalSeconds:scene.startSeconds+at,label:result.label,screenshot});
   await page.screenshot({path:path.join(out,screenshot)});
  }
 }
}
await browser.close();
await fs.writeFile(path.join(out,'report.json'),JSON.stringify({states:checks.length,errors,checks},null,2));
console.log(JSON.stringify({states:checks.length,errors},null,2));
if(errors.length)process.exitCode=1;
