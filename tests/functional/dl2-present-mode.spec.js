// Present mode fits every DL2 slide on a classroom projector (2026-09-26 projector fix).
// Source: courses/digital-literacy-2/assets/lesson.js and assets/present.css.
const {test,expect}=require('@playwright/test');
const base='/courses/digital-literacy-2';
const deck=n=>`${base}/weeks/week-0${n}/presentation.html`;
const screens=[[1024,768],[1280,720],[1366,768],[1920,1080]];

// For the visible slide: is all of it inside the card, does anything inside scroll, and how large is body text?
// Wait until the visible slide's pictures and video know their size, as a presenter would see it.
const settle=page=>page.waitForFunction(()=>{const s=document.querySelector('.slide:not([hidden])');
 return [...s.querySelectorAll('img')].every(i=>i.complete)&&[...s.querySelectorAll('video')].every(v=>v.readyState>=1);},null,{timeout:5000}).catch(()=>{})
 .then(()=>page.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))));
const measure=async page=>{await settle(page);return page.evaluate(()=>{
 // Every slide is one fixed card (2026-09-28 deck redesign): its body is scaled to fit, never scrolled or clipped.
 // On a 4:3 1024×768 projector one Week 6 slide (flip cards plus the three-part app window) scales to about 11px text.
 const s=document.querySelector('.slide:not([hidden])'),b=s.querySelector('.slide-body');
 const box=s.getBoundingClientRect(),cs=getComputedStyle(s);
 const room={bottom:box.bottom-parseFloat(cs.paddingBottom),right:box.right-parseFloat(cs.paddingRight)};
 const r=b?b.getBoundingClientRect():box;
 const fit=Number(s.dataset.fit||1);
 const body=[...s.querySelectorAll('.slide-subtitle, .key-point-text, .check-options button, .step-list li>button>span:first-child')].filter(e=>e.offsetParent);
 const smallest=body.length?Math.min(...body.map(e=>parseFloat(getComputedStyle(e).fontSize)*fit)):24;
 const overflowing=[...s.querySelectorAll('*')].some(e=>e.scrollHeight>e.clientHeight+2&&/(auto|scroll)/.test(getComputedStyle(e).overflowY)&&e.clientHeight>0);
 const clipped=!!b&&b.scrollHeight*fit>s.clientHeight+2;
 return {id:s.id,framed:!!b,top:r.top,bottom:r.bottom,roomBottom:room.bottom,roomRight:room.right,right:r.right,smallest,overflowing,clipped,fit};
});};

for(const [w,h] of screens)test(`Present mode fits every slide at ${w}×${h}`,async({page})=>{
 test.setTimeout(120_000);
 await page.setViewportSize({width:w,height:h});await page.emulateMedia({reducedMotion:'reduce'});
 const misfits=[];
 for(let n=1;n<=6;n++){
  await page.goto(deck(n));await page.keyboard.press('p');await expect(page.locator('body')).toHaveClass(/presenting/);
  const count=await page.locator('.slide').count();
  for(let i=1;i<=count;i++){
   await page.locator('[data-slide]').nth(i-1).evaluate(b=>b.click());
   const m=await measure(page);
   if(!m.framed||m.top<-1||m.bottom>m.roomBottom+2||m.right>m.roomRight+2||m.overflowing||m.clipped||m.smallest<(w===1024?11:13)||m.fit<0.5)misfits.push(`week ${n} ${m.id}: content bottom ${Math.round(m.bottom)} / room ${Math.round(m.roomBottom)}, fit ${m.fit}, text ${m.smallest.toFixed(1)}px${m.overflowing?', scrolls inside':''}${m.clipped?', clipped':''}`);
  }
 }
 expect(misfits,misfits.join('\n')).toEqual([]);
});

test('Present mode turns on with P or the Present button and off with Escape or P',async({page})=>{
 await page.setViewportSize({width:1366,height:768});await page.goto(deck(1));
 const body=page.locator('body');
 await expect(body).not.toHaveClass(/presenting/);await expect(page.locator('.sidebar')).toBeVisible();
 await page.getByRole('button',{name:/Present/}).click();await expect(body).toHaveClass(/presenting/);
 await expect(page.locator('.sidebar')).toBeHidden();await expect(page.locator('.topbar')).toBeHidden();
 // Slide 3 fits in one part, so the next key moves straight to slide 4.
 await page.locator('[data-slide="2"]').evaluate(b=>b.click());await page.keyboard.press('ArrowRight');await expect(page.locator('#slide-4')).toBeVisible();
 await page.keyboard.press('Escape');await expect(body).not.toHaveClass(/presenting/);await expect(page.locator('.sidebar')).toBeVisible();
 await expect.poll(()=>page.evaluate(()=>!!document.fullscreenElement)).toBe(false);
 // Let the switch to full screen finish before the second press, as a person would.
 const settled=()=>page.waitForFunction(()=>!!document.fullscreenElement,null,{timeout:2000}).catch(()=>{})
  .then(()=>page.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))));
 await page.keyboard.press('p');await expect(body).toHaveClass(/presenting/);await settled();
 await page.keyboard.press('p');await expect(body).not.toHaveClass(/presenting/);
 await expect.poll(()=>page.evaluate(()=>!!document.fullscreenElement)).toBe(false);
});

test('Leaving present mode puts every slide back exactly as it was',async({page})=>{
 await page.setViewportSize({width:1366,height:768});await page.goto(deck(3));
 const snapshot=()=>page.evaluate(()=>[...document.querySelectorAll('.slide')].map(s=>[...s.children].map(c=>c.tagName+'.'+c.className).join('|')).join('\n'));
 const before=await snapshot();
 await page.keyboard.press('p');await expect(page.locator('body')).toHaveClass(/presenting/);
 await page.keyboard.press('Escape');await expect(page.locator('body')).not.toHaveClass(/presenting/);
 expect(await snapshot()).toBe(before);
});

test('Typing P inside a form field does not start present mode',async({page})=>{
 await page.goto(deck(3));const id=await page.locator('.slide:has(#paper-cost)').getAttribute('id');
 await page.goto(deck(3)+'#'+id);await page.locator('#paper-cost').focus();await expect(page.locator('#paper-cost')).toBeFocused();await page.keyboard.press('p');
 await expect(page.locator('body')).not.toHaveClass(/presenting/);
});

test('Interactions still work in present mode',async({page})=>{
 await page.setViewportSize({width:1366,height:768});await page.goto(deck(1)+'#slide-16');await page.keyboard.press('p');
 await page.locator('#slide-16 .check-options button').nth(2).click();
 await expect(page.locator('#slide-16 .feedback')).toContainText('Correct');
});

test('Restarting right after Escape keeps presenting when the earlier full screen finishes closing',async({page})=>{
 await page.setViewportSize({width:1366,height:768});await page.goto(deck(2));
 const body=page.locator('body');
 await page.keyboard.press('p');await page.waitForFunction(()=>!!document.fullscreenElement,null,{timeout:2000}).catch(()=>{});
 await page.keyboard.press('Escape');await page.keyboard.press('p');
 await page.waitForTimeout(600); // let the earlier exit's full-screen signal arrive
 await expect(body).toHaveClass(/presenting/);
});

test('Words stay readable against every slide background in present mode',async({page})=>{
 test.setTimeout(120_000);
 await page.setViewportSize({width:1920,height:1080});
 const bad=[];
 for(let n=1;n<=6;n++){
  await page.goto(deck(n));await page.keyboard.press('p');
  const count=await page.locator('.slide').count();
  for(let i=0;i<count;i++){
   await page.locator('[data-slide]').nth(i).evaluate(b=>b.click());
   bad.push(...await page.evaluate(()=>{
    const lum=c=>{const [r,g,b]=c.match(/[\d.]+/g).slice(0,3).map(Number).map(v=>{v/=255;return v<=0.03928?v/12.92:((v+0.055)/1.055)**2.4;});return 0.2126*r+0.7152*g+0.0722*b;};
    const ratio=(a,b)=>{const [x,y]=[lum(a),lum(b)].sort((m,k)=>k-m);return (x+0.05)/(y+0.05);};
    const s=document.querySelector('.slide:not([hidden])');const out=[];
    for(const p of s.querySelectorAll('.present-copy > p, .present-copy .slide-lead')){
     if(!p.offsetParent)continue;let bg='rgb(255, 255, 255)';
     for(let e=p;e;e=e.parentElement){const c=getComputedStyle(e).backgroundColor;if(!/rgba\(.*,\s*0\)$|transparent/.test(c)){bg=c;break;}}
     const r=ratio(getComputedStyle(p).color,bg);if(r<4.5)out.push(`${s.id}: ${r.toFixed(2)}:1 "${p.textContent.slice(0,40)}"`);
    }return out;}).then(x=>x.map(y=>`week ${n} ${y}`)));
  }
 }
 expect(bad,bad.join('\n')).toEqual([]);
});

test('Present mode passes an accessibility scan',async({page})=>{
 const AxeBuilder=require('@axe-core/playwright').default;
 await page.setViewportSize({width:1366,height:768});
 for(const [n,slide] of [[1,7],[4,17],[3,15]]){
  await page.goto(deck(n)+'#slide-'+slide);await page.keyboard.press('p');await expect(page.locator('body')).toHaveClass(/presenting/);
  const result=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();
  expect(result.violations.map(v=>({id:v.id,nodes:v.nodes.map(x=>x.target)})),`week ${n} slide ${slide}`).toEqual([]);
 }
});

// Week 1 is taught from a lean deck (2026-09-27 units rebuild): on a 16:9 projector no slide has to shrink
// its text to fit; sparse slides scale up to fill the card.
for(const [w,h] of [[1280,720],[1366,768]])test(`Week 1 never shrinks a slide hard at ${w}×${h}`,async({page})=>{
 await page.setViewportSize({width:w,height:h});await page.emulateMedia({reducedMotion:'reduce'});
 await page.goto(deck(1));await page.keyboard.press('p');await expect(page.locator('body')).toHaveClass(/presenting/);
 const count=await page.locator('.slide').count();const small=[];
 for(let i=1;i<=count;i++){
  await page.locator('[data-slide]').nth(i-1).evaluate(b=>b.click());await settle(page);
  const s=await page.evaluate(()=>{const s=document.querySelector('.slide:not([hidden])');return {id:s.id,fit:Number(s.dataset.fit||1)};});
  if(s.fit<0.85)small.push(`${s.id} (fit ${s.fit})`);
 }
 expect(small,small.join(', ')).toEqual([]);
});
