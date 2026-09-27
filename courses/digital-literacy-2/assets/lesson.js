(() => {
  'use strict';
  document.documentElement.classList.add('js');
  const slides = [...document.querySelectorAll('.slide')];
  const week = Number(document.body.dataset.week);
  const links = [...document.querySelectorAll('[data-slide]')];
  const counter = document.querySelector('#slide-counter');
  const progress = document.querySelector('#lesson-progress');
  let index = 0;
  let fit = () => {}; // set below; show() refits after every slide change
  function hashIndex() { const found = slides.findIndex(s => '#'+s.id === location.hash); return found; }
  function show(next, focus = false, write = true) {
    index = Math.max(0, Math.min(slides.length-1,next));
    slides.forEach((s,i) => { s.hidden = i !== index; if (i !== index) s.querySelectorAll('video').forEach(v=>v.pause()); });
    links.forEach((l,i)=>{l.setAttribute('aria-current',String(i===index));if(i<index)l.classList.add('seen');});
    counter.textContent = `Slide ${index+1} of ${slides.length}`;
    const pt=document.querySelector('#progress-text');if(pt)pt.textContent=`${Math.round((index+1)/slides.length*100)}% complete`;
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
    const go=d=>show(index+d,true);
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
    document.querySelector('.main-content').addEventListener('touchstart',e=>{if(!e.target.closest('input,button,a,select,video,.calendar-surface'))touch=[e.changedTouches[0].clientX,e.changedTouches[0].clientY];},{passive:true});
    document.querySelector('.main-content').addEventListener('touchend',e=>{if(!touch)return;const dx=e.changedTouches[0].clientX-touch[0],dy=e.changedTouches[0].clientY-touch[1];if(Math.abs(dx)>90&&Math.abs(dy)<50)go(dx<0?1:-1);touch=null;},{passive:true});
    document.querySelector('.menu-toggle').addEventListener('click',e=>{const open=document.querySelector('.sidebar').classList.toggle('open');e.currentTarget.setAttribute('aria-expanded',String(open));});
    // Every slide is one fixed screen, like a projected slide: it never scrolls. A slide with little on it
    // is scaled up (to MAX_FIT) so it fills the card; one with too much is scaled down, never below
    // MIN_FIT, so text stays readable. Present mode hides the chrome and goes full screen; the slide
    // itself does not change.
    const MIN_FIT=0.5,MAX_FIT=1.55;
    let reachedFullscreen=false,startedAt=0; // this presentation actually went full screen, and when it began
    const presenting=()=>document.body.classList.contains('presenting');
    fit=function(){
      const s=slides[index],b=s.querySelector('.slide-body');if(!b)return;
      b.style.zoom='';b.style.minHeight='';
      const cs=getComputedStyle(s);
      const room=s.clientHeight-parseFloat(cs.paddingTop)-parseFloat(cs.paddingBottom);
      const full=s.matches('.title-slide,.completion-slide,.summary-slide');
      // Width only ever limits a scale-down: at zoom 1 the body already fills the slide's width.
      let scale=Math.min(full?1:MAX_FIT,(room-2)/Math.max(1,b.scrollHeight));
      if(b.scrollWidth>s.clientWidth+1)scale=Math.min(scale,s.clientWidth/b.scrollWidth);
      // Screen-relative sizes inside (video, photos) do not shrink with zoom: measure and adjust.
      const limit=s.getBoundingClientRect().bottom-parseFloat(cs.paddingBottom)-1;
      scale=Math.max(MIN_FIT,scale);
      for(let i=0;i<9;i++){
        b.style.zoom=Math.abs(scale-1)>0.01?String(scale):'';
        const over=b.getBoundingClientRect().bottom-limit;
        if(over<=0||scale<=MIN_FIT)break;
        const height=b.getBoundingClientRect().height;
        scale=Math.max(MIN_FIT,scale*(height-over)/height-0.006);
      }
      // The body then fills the card at that scale, so rows of cards and tiles spread down the slide.
      b.style.minHeight=Math.floor(room/scale-2)+'px';
      s.dataset.fit=scale.toFixed(3);
    };
    function present(on){
      document.body.classList.toggle('presenting',on);
      if(on){
        reachedFullscreen=false;startedAt=Date.now();
        window.scrollTo(0,0);
        document.documentElement.requestFullscreen?.().catch(()=>{});
        fit();slides[index].querySelector('h2').focus({preventScroll:true});
      } else {
        if(document.fullscreenElement)document.exitFullscreen?.().catch(()=>{});
        fit();document.querySelector('#present')?.focus({preventScroll:true});
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
      // An exit signal from a presentation that ended a moment ago must not end the one just restarted.
      else if(presenting()&&reachedFullscreen&&Date.now()-startedAt>800)present(false);
    });
    window.addEventListener('resize',fit);
    fit();
    // A click inside a slide (a practice control, a check answer) refits only if the slide now overflows.
    document.querySelector('.main-content').addEventListener('click',()=>setTimeout(()=>{const s=slides[index],b=s.querySelector('.slide-body');if(!b)return;const limit=s.getBoundingClientRect().bottom-parseFloat(getComputedStyle(s).paddingBottom);if(b.getBoundingClientRect().bottom>limit+1)fit();},0));
    document.querySelector('.main-content').addEventListener('toggle',()=>fit(),true);
    // Pictures and video only know their size once loaded: choose the slide's arrangement again.
    const relayout=()=>fit();
    document.querySelector('.main-content').addEventListener('load',relayout,true);
    document.querySelector('.main-content').addEventListener('loadedmetadata',relayout,true);
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
