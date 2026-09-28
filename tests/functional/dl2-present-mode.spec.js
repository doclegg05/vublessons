// Present mode fits every DL2 slide on a classroom projector (2026-09-26 projector fix).
// Source: courses/digital-literacy-2/assets/lesson.js and assets/present.css.
const {test,expect}=require('@playwright/test');
const base='/courses/digital-literacy-2';
const deck=n=>`${base}/weeks/week-0${n}/presentation.html`;
const screens=[[1024,768],[1280,720],[1366,768],[1920,1080]];

// For the visible slide: is all of it on screen, does anything inside scroll, and how large is body text?
// Wait until the visible slide's pictures and video know their size, as a presenter would see it.
const settle=page=>page.waitForFunction(()=>{const s=document.querySelector('.slide:not([hidden])');
 return [...s.querySelectorAll('img')].every(i=>i.complete)&&[...s.querySelectorAll('video')].every(v=>v.readyState>=1);},null,{timeout:5000}).catch(()=>{})
 .then(()=>page.evaluate(()=>new Promise(r=>requestAnimationFrame(()=>requestAnimationFrame(r)))));
const measure=async page=>{await settle(page);return page.evaluate(()=>{
 // Measure the slide's content (the present frame), not the slide box: the box is always screen height.
 const s=document.querySelector('.slide:not([hidden])'),f=s.querySelector('.present-frame');
 const box=s.getBoundingClientRect(),cs=getComputedStyle(s);
 const room={bottom:box.bottom-parseFloat(cs.paddingBottom),right:box.right-parseFloat(cs.paddingRight)};
 const r=f?f.getBoundingClientRect():box;
 const fit=Number(s.dataset.fit||1);
 const body=[...s.querySelectorAll('.slide-lead, .present-copy > p, .check-options button')].filter(e=>e.offsetParent);
 const smallest=body.length?Math.min(...body.map(e=>parseFloat(getComputedStyle(e).fontSize)*fit)):32;
 const bar=document.querySelector('.bottom-nav').getBoundingClientRect();
 const overflowing=[...s.querySelectorAll('*')].some(e=>e.scrollHeight>e.clientHeight+2&&/(auto|scroll)/.test(getComputedStyle(e).overflowY)&&e.clientHeight>0);
 return {id:s.id,framed:!!f,top:r.top,bottom:r.bottom,roomBottom:Math.min(room.bottom,bar.top),roomRight:room.right,right:r.right,smallest,overflowing,fit};
});};

// Narrowed 2026-09-28 (Mission Control, Task 11): weeks 2–6 here. Week 1's replaced deck has its own fit checks at
// 1920×1080 and every text size (tests/functional/dl2-os-week1-deck.spec.js).
for(const [w,h] of screens)test(`Present mode fits every slide at ${w}×${h}`,async({page})=>{
 test.setTimeout(120_000);
 await page.setViewportSize({width:w,height:h});await page.emulateMedia({reducedMotion:'reduce'});
 const misfits=[];
 for(let n=2;n<=6;n++){
  await page.goto(deck(n));await page.keyboard.press('p');await expect(page.locator('body')).toHaveClass(/presenting/);
  const count=await page.locator('.slide').count();
  for(let i=1;i<=count;i++){
   await page.locator('[data-slide]').nth(i-1).evaluate(b=>b.click());
   // A build slide shows one part at a time; every part must fit.
   for(let part=1;;part++){
    const m=await measure(page);
    if(!m.framed||m.top<-1||m.bottom>m.roomBottom+1||m.right>m.roomRight+1||m.overflowing||m.smallest<24)misfits.push(`week ${n} ${m.id} part ${part}: content bottom ${Math.round(m.bottom)} / room ${Math.round(m.roomBottom)}, fit ${m.fit}, text ${m.smallest.toFixed(1)}px${m.overflowing?', scrolls inside':''}`);
    const more=await page.evaluate(()=>{const s=document.querySelector('.slide:not([hidden])');return s.dataset.layout==='build'&&Number(s.dataset.step)<Number(s.dataset.steps)-1;});
    if(!more)break;
    await page.keyboard.press('ArrowRight');
    expect(await page.evaluate(()=>document.querySelector('.slide:not([hidden])').id)).toBe(m.id);
   }
  }
 }
 expect(misfits,misfits.join('\n')).toEqual([]);
});

// Restored 2026-09-28 (final review): these two ran on the replaced week 1 deck and were retired in Task 11. Present
// mode lives in the shared assets/lesson.js engine that weeks 2-6 still use, so they now run on week 2.
test('Present mode turns on with P or the Present button and off with Escape or P',async({page})=>{
 await page.setViewportSize({width:1366,height:768});await page.goto(deck(2));
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

test('Interactions still work in present mode',async({page})=>{
 await page.setViewportSize({width:1366,height:768});await page.goto(deck(2)+'#slide-19');await page.keyboard.press('p');
 await page.locator('#slide-19 .check-options button').nth(2).click();
 await expect(page.locator('#slide-19 .feedback')).toContainText('Correct');
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

test('A slide too tall for the screen is shown one part at a time, words first',async({page})=>{
 await page.setViewportSize({width:1024,height:768});await page.goto(deck(4)+'#slide-17');await page.keyboard.press('p');
 const slide=page.locator('#slide-17');
 await expect(slide).toHaveAttribute('data-layout','build');
 const n=Number(await slide.getAttribute('data-steps'));expect(n).toBeGreaterThan(1);
 await expect(slide.locator('.present-copy')).toBeVisible();await expect(page.locator('#slide-counter')).toHaveText(`Slide 17 of 23 · part 1 of ${n}`);
 for(let k=2;k<=n;k++){await page.keyboard.press('ArrowRight');await expect(page.locator('#slide-counter')).toHaveText(`Slide 17 of 23 · part ${k} of ${n}`);}
 await expect(slide.locator('.present-copy')).toBeHidden();
 await page.keyboard.press('ArrowRight');await expect(page.locator('#slide-18')).toBeVisible();
 await page.keyboard.press('ArrowLeft');await expect(page.locator('#slide-counter')).toHaveText(`Slide 17 of 23 · part ${n} of ${n}`);
});

test('Restarting right after Escape keeps presenting when the earlier full screen finishes closing',async({page})=>{
 await page.setViewportSize({width:1366,height:768});await page.goto(deck(2));
 const body=page.locator('body');
 await page.keyboard.press('p');await page.waitForFunction(()=>!!document.fullscreenElement,null,{timeout:2000}).catch(()=>{});
 await page.keyboard.press('Escape');await page.keyboard.press('p');
 await page.waitForTimeout(600); // let the earlier exit's full-screen signal arrive
 await expect(body).toHaveClass(/presenting/);
});

// Narrowed 2026-09-28 (Mission Control, Task 11): weeks 2–6; week 1's replaced deck has no present mode.
test('Words stay readable against every slide background in present mode',async({page})=>{
 test.setTimeout(120_000);
 await page.setViewportSize({width:1920,height:1080});
 const bad=[];
 for(let n=2;n<=6;n++){
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

// Narrowed 2026-09-28 (Mission Control, Task 11): week 1 slide 7 dropped with the replaced deck.
test('Present mode passes an accessibility scan',async({page})=>{
 const AxeBuilder=require('@axe-core/playwright').default;
 await page.setViewportSize({width:1366,height:768});
 for(const [n,slide] of [[4,17],[3,15]]){
  await page.goto(deck(n)+'#slide-'+slide);await page.keyboard.press('p');await expect(page.locator('body')).toHaveClass(/presenting/);
  const result=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();
  expect(result.violations.map(v=>({id:v.id,nodes:v.nodes.map(x=>x.target)})),`week ${n} slide ${slide}`).toEqual([]);
 }
});
