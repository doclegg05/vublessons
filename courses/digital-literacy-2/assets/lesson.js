(() => {
  'use strict';
  document.documentElement.classList.add('js');
  const slides = [...document.querySelectorAll('.slide')];
  const week = Number(document.body.dataset.week);
  const links = [...document.querySelectorAll('[data-slide]')];
  const counter = document.querySelector('#slide-counter');
  const progress = document.querySelector('#lesson-progress');
  let index = 0;
  let fit = () => {}; // set by present mode below; show() refits after every slide change
  let stepWithin = () => false; // present mode: step through a slide's parts before changing slide
  function hashIndex() { const found = slides.findIndex(s => '#'+s.id === location.hash); return found; }
  function show(next, focus = false, write = true) {
    index = Math.max(0, Math.min(slides.length-1,next));
    slides.forEach((s,i) => { s.hidden = i !== index; if (i !== index) s.querySelectorAll('video').forEach(v=>v.pause()); });
    links.forEach((l,i)=>l.setAttribute('aria-current',String(i===index)));
    counter.textContent = `Slide ${index+1} of ${slides.length}`;
    progress.value=index+1; progress.max=slides.length;
    document.querySelector('#previous').disabled=index===0;
    document.querySelector('#next').disabled=index===slides.length-1;
    if(write) history.replaceState(null,'','#'+slides[index].id);
    window.VubProgress?.saveSlide('dl2',week,index,slides.length);
    if(focus) { const h=slides[index].querySelector('h2'); h.focus({preventScroll:true}); slides[index].scrollIntoView({block:'start',behavior:'instant'}); }
    if(focus||write) links[index]?.scrollIntoView({block:'nearest',behavior:'instant'});
    fit();
  }
  if(slides.length) {
    const saved=window.VubProgress?.get('dl2',week)?.slide;
    show(hashIndex()>=0?hashIndex():Number.isInteger(saved)?saved:0,false,false);
    links.forEach(b=>b.addEventListener('click',()=>{show(Number(b.dataset.slide),true); document.querySelector('.sidebar').classList.remove('open'); document.querySelector('.menu-toggle').setAttribute('aria-expanded','false');}));
    const go=d=>{if(stepWithin(d))return;const from=index;show(index+d,true);if(d<0&&index!==from)stepWithin('last');};
    document.querySelector('#previous').addEventListener('click',()=>go(-1));
    document.querySelector('#next').addEventListener('click',()=>go(1));
    document.querySelector('#restart').addEventListener('click',()=>show(0,true));
    window.addEventListener('hashchange',()=>{if(hashIndex()>=0)show(hashIndex(),true,false);});
    document.addEventListener('keydown',e=>{
      if(e.altKey||e.ctrlKey||e.metaKey||e.shiftKey||e.target.closest('input,textarea,select,summary,video,[contenteditable],[tabindex="0"]'))return;
      const d={ArrowRight:1,PageDown:1,ArrowLeft:-1,PageUp:-1}[e.key];
      if(d){e.preventDefault();go(d);return;}
      const dest={Home:0,End:slides.length-1}[e.key];
      if(dest!==undefined){e.preventDefault();show(dest,true);}
    });
    let touch=null;
    document.querySelector('.deck-main').addEventListener('touchstart',e=>{if(!e.target.closest('input,button,a,select,video,.calendar-surface'))touch=[e.changedTouches[0].clientX,e.changedTouches[0].clientY];},{passive:true});
    document.querySelector('.deck-main').addEventListener('touchend',e=>{if(!touch)return;const dx=e.changedTouches[0].clientX-touch[0],dy=e.changedTouches[0].clientY-touch[1];if(Math.abs(dx)>90&&Math.abs(dy)<50)go(dx<0?1:-1);touch=null;},{passive:true});
    document.querySelector('.menu-toggle').addEventListener('click',e=>{const open=document.querySelector('.sidebar').classList.toggle('open');e.currentTarget.setAttribute('aria-expanded',String(open));});
    // Present mode fits one slide to a projector: text on the left, visuals on the right. The frame
    // scales down only while 32px slide text stays at 24px or more. Leaving restores every slide.
    const STAGE='figure.scenario-photo,.topic-scene,.workshop,.authored-window,.flip-grid,video,.video-caption,.video-chapters,.step-list,.evidence-sequence,form.exercise,div.exercise,.interactive-calc';
    const MIN_FIT=0.75, original=new Map();
    let reachedFullscreen=false; // this presentation actually went full screen
    const presenting=()=>document.body.classList.contains('presenting');
    function frame(s){
      if(original.has(s))return;
      original.set(s,[...s.children].map(k=>[k,k.getAttribute('class')]));
      const f=document.createElement('div'),copy=document.createElement('div'),stage=document.createElement('div');
      f.className='present-frame';copy.className='present-copy';stage.className='present-stage';
      [...s.children].forEach(c=>(c.tagName==='H2'?f:c.matches(STAGE)?stage:copy).append(c));
      if(copy.children.length)f.append(copy);
      if(stage.children.length)f.append(stage);
      f.classList.toggle('no-stage',!stage.children.length);f.classList.toggle('no-copy',!copy.children.length);
      s.append(f);
    }
    function unframe(s){
      if(!original.has(s))return;
      const kids=original.get(s);kids.forEach(([k,cls])=>cls===null?k.removeAttribute('class'):k.setAttribute('class',cls));
      s.replaceChildren(...kids.map(([k])=>k));original.delete(s);
      ['fit','layout','layoutFor','step','steps'].forEach(k=>delete s.dataset[k]);
    }
    // A build shows one part at a time: the words first, then each visual.
    const parts=s=>{const f=s.querySelector('.present-frame');return [f.querySelector('.present-copy'),...(f.querySelector('.present-stage')?.children||[])].filter(Boolean);};
    const groups=new WeakMap(); // slide -> [[part indexes shown together], ...] while in build layout
    function applyStep(s){
      const f=s.querySelector('.present-frame'),all=parts(s),build=s.dataset.layout==='build';
      const steps=build?(groups.get(s)||all.map((_,i)=>[i])):[all.map((_,i)=>i)];
      const k=Math.min(Number(s.dataset.step||0),steps.length-1),shown=steps[k];
      all.forEach((v,i)=>v.classList.toggle('build-hidden',!shown.includes(i)));
      const words=shown.some(i=>all[i].classList.contains('present-copy'));
      // Words with visuals use the two columns; visuals on their own use the full width.
      f.classList.toggle('build',build&&!(words&&shown.length>1));
      f.classList.toggle('visual-part',build&&!words);
      s.dataset.steps=steps.length;
      counter.textContent=`Slide ${index+1} of ${slides.length}`+(build?` · part ${k+1} of ${steps.length}`:'');
    }
    function setLayout(s,f,layout){s.dataset.layout=layout;f.classList.toggle('stacked',layout==='stack');f.classList.toggle('build',layout==='build');applyStep(s);}
    function scaleOf(s,f){
      f.style.zoom='';
      const cs=getComputedStyle(s),room=s.clientHeight-parseFloat(cs.paddingTop)-parseFloat(cs.paddingBottom);
      return Math.min(1,(room-6)/f.scrollHeight,f.clientWidth/Math.max(1,f.scrollWidth));
    }
    let shown=-1;
    fit=function(){
      if(!presenting())return;
      const s=slides[index],f=s.querySelector('.present-frame');if(!f)return;
      if(shown!==index){s.dataset.step=0;shown=index;}
      const screen=innerWidth+'x'+innerHeight;
      if(s.dataset.layoutFor!==screen){
        let best='side';setLayout(s,f,'side');let scale=scaleOf(s,f);
        if(scale<1&&!f.matches('.no-stage,.no-copy')){setLayout(s,f,'stack');const t=scaleOf(s,f);if(t>scale+0.01){best='stack';scale=t;}}
        if(scale<MIN_FIT&&parts(s).length>1){
          // Pack parts in order into as few steps as fit at the text floor.
          setLayout(s,f,'build');const all=parts(s),packed=[[0]];
          const fits=g=>{groups.set(s,[g]);s.dataset.step=0;applyStep(s);return scaleOf(s,f);};
          for(let i=1;i<all.length;i++){const last=packed[packed.length-1];if(fits([...last,i])>=MIN_FIT)last.push(i);else packed.push([i]);}
          const worst=Math.min(...packed.map(fits));
          groups.set(s,packed);s.dataset.step=0;
          if(worst>scale)best='build';else groups.delete(s);
        }
        setLayout(s,f,best);s.dataset.layoutFor=screen;
      }
      applyStep(s);
      // Screen-relative sizes (video and photo limits) do not shrink with zoom, so set a scale,
      // measure where the content really ends, and adjust until it fits or reaches the text floor.
      const cs=getComputedStyle(s),limit=s.getBoundingClientRect().bottom-parseFloat(cs.paddingBottom)-2;
      let scale=Math.max(MIN_FIT,scaleOf(s,f));
      for(let i=0;i<6;i++){
        f.style.zoom=String(scale);
        const over=f.getBoundingClientRect().bottom-limit;
        if(over<=0||scale<=MIN_FIT)break;
        const height=f.getBoundingClientRect().height;
        scale=Math.max(MIN_FIT,scale*(height-over)/height-0.004);
      }
      s.dataset.fit=scale.toFixed(3);
    };
    stepWithin=function(d){
      if(!presenting())return false;
      const s=slides[index];if(s.dataset.layout!=='build')return false;
      const n=Number(s.dataset.steps||1),k=d==='last'?n-1:Number(s.dataset.step||0)+d;
      if(k<0||k>=n)return false;
      s.dataset.step=k;fit();s.querySelector('h2').focus({preventScroll:true});return true;
    };
    function present(on){
      document.body.classList.toggle('presenting',on);
      slides.forEach(on?frame:unframe);
      if(on){
        reachedFullscreen=false;
        window.scrollTo(0,0);
        document.documentElement.requestFullscreen?.().catch(()=>{});
        fit();slides[index].querySelector('h2').focus({preventScroll:true});
      } else {
        if(document.fullscreenElement)document.exitFullscreen?.().catch(()=>{});
        document.querySelector('#present')?.focus({preventScroll:true});
      }
    }
    document.querySelector('#present')?.addEventListener('click',()=>present(true));
    document.querySelector('#present-exit')?.addEventListener('click',()=>present(false));
    document.addEventListener('keydown',e=>{
      if(e.altKey||e.ctrlKey||e.metaKey||e.target.closest('input,textarea,select,[contenteditable]'))return;
      if(e.key==='p'||e.key==='P'){e.preventDefault();present(!presenting());}
      else if(e.key==='Escape'&&presenting())present(false);
    });
    // The browser's own Esc leaves full screen; leave present mode with it. If full screen arrives after
    // present mode was already turned off (P pressed twice quickly), leave full screen too.
    // A late signal from an earlier exit must not end a presentation that has just restarted.
    document.addEventListener('fullscreenchange',()=>{
      if(document.fullscreenElement){if(presenting())reachedFullscreen=true;else document.exitFullscreen?.().catch(()=>{});}
      else if(presenting()&&reachedFullscreen)present(false);
    });
    window.addEventListener('resize',fit);
    document.querySelector('.deck-main').addEventListener('click',()=>setTimeout(fit,0));
    document.querySelector('.deck-main').addEventListener('toggle',()=>fit(),true);
    // Pictures and video only know their size once loaded; refit when they do.
    // Pictures and video only know their size once loaded: choose the slide's arrangement again.
    const relayout=()=>{if(presenting()){delete slides[index].dataset.layoutFor;fit();}};
    document.querySelector('.deck-main').addEventListener('load',relayout,true);
    document.querySelector('.deck-main').addEventListener('loadedmetadata',relayout,true);
  }
  document.querySelectorAll('.flip').forEach(b=>b.addEventListener('click',()=>{const open=b.getAttribute('aria-expanded')!=='true';b.setAttribute('aria-expanded',String(open));b.querySelector('.flip-front').setAttribute('aria-hidden',String(open));b.querySelector('.flip-back').setAttribute('aria-hidden',String(!open));}));
  document.querySelectorAll('.check-options').forEach(group=>group.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{group.querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));const ok=b.dataset.correct==='true';group.nextElementSibling.textContent=(ok?'Correct. ':'Try again. ')+(ok?group.dataset.explanation:'Think about the task and choose another answer.');})));
  document.querySelectorAll('[data-print]').forEach(b=>b.addEventListener('click',()=>window.print()));
  document.querySelectorAll('.worksheet-input').forEach(t=>{t.addEventListener('input',()=>{t.nextElementSibling.textContent=t.value;t.style.height='auto';t.style.height=t.scrollHeight+'px';});});
  const answers=[...document.querySelectorAll('.worksheet-input')];
  if(answers.length) window.addEventListener('beforeunload',e=>{if(answers.some(t=>t.value.trim())){e.preventDefault();e.returnValue='';}});
  const form=document.querySelector('#practice-form');
  form?.addEventListener('submit',e=>{e.preventDefault();document.querySelector('#form-result').textContent=`Practice complete: ${form.elements.topic.value}; ${form.elements.method.value}. No request was sent. Review your choices or reset to try again.`;});
  form?.addEventListener('reset',()=>document.querySelector('#form-result').textContent='');
  const permission=document.querySelector('#permission');
  permission?.addEventListener('change',()=>{document.querySelector('#permission-result').textContent={viewer:'Viewer: Alex can read this fictional file. They cannot edit it.',commenter:'Commenter: Alex can suggest clearer wording. You decide which edits to make.',editor:'Editor: Alex can change the fictional file. Use this only for coauthoring.'}[permission.value]||'Choose a permission.';});
  const paper=document.querySelector('#paper-cost');
  const updateBudget=()=>{
    const n=Number(paper.value);const valid=paper.value!==''&&Number.isFinite(n)&&n>=0;
    const total=valid?(n+8+5).toFixed(2):null;
    document.querySelector('#budget-total').textContent=valid?`Total: $${total}`:'Enter a nonnegative paper cost.';
    document.querySelectorAll('[data-budget-paper]').forEach(cell=>{cell.textContent=valid?n.toFixed(2):'—';});
    document.querySelectorAll('[data-budget-sum]').forEach(cell=>{cell.textContent=valid?total:'—';});
  };
  if(paper){paper.addEventListener('input',updateBudget);updateBudget();}
  document.querySelectorAll('[data-week-status]').forEach(el=>{const p=window.VubProgress?.get('dl2',el.dataset.weekStatus);el.textContent=p?.completed?'Lesson viewed to the end':p?`Resume at slide ${p.slide+1}`:'Ready to begin';});
})();
