(() => {
  'use strict';
  document.documentElement.classList.add('js');
  const slides = [...document.querySelectorAll('.slide')];
  const week = Number(document.body.dataset.week);
  const links = [...document.querySelectorAll('[data-slide]')];
  const counter = document.querySelector('#slide-counter');
  const progress = document.querySelector('#lesson-progress');
  let index = 0;
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
    links[index]?.scrollIntoView({block:'nearest',behavior:'instant'});
  }
  if(slides.length) {
    const saved=window.VubProgress?.get('dl2',week)?.slide;
    show(hashIndex()>=0?hashIndex():Number.isInteger(saved)?saved:0,false);
    links.forEach(b=>b.addEventListener('click',()=>{show(Number(b.dataset.slide),true); document.querySelector('.sidebar').classList.remove('open'); document.querySelector('.menu-toggle').setAttribute('aria-expanded','false');}));
    document.querySelector('#previous').addEventListener('click',()=>show(index-1,true));
    document.querySelector('#next').addEventListener('click',()=>show(index+1,true));
    document.querySelector('#restart').addEventListener('click',()=>show(0,true));
    window.addEventListener('hashchange',()=>{if(hashIndex()>=0)show(hashIndex(),true,false);});
    document.addEventListener('keydown',e=>{
      if(e.altKey||e.ctrlKey||e.metaKey||e.shiftKey||e.target.closest('input,textarea,select,button,a,summary,video,[contenteditable]'))return;
      const dest={ArrowRight:index+1,PageDown:index+1,ArrowLeft:index-1,PageUp:index-1,Home:0,End:slides.length-1}[e.key];
      if(dest!==undefined){e.preventDefault();show(dest,true);}
    });
    let touch=null;
    document.querySelector('.deck-main').addEventListener('touchstart',e=>{if(!e.target.closest('input,button,a,select,video'))touch=[e.changedTouches[0].clientX,e.changedTouches[0].clientY];},{passive:true});
    document.querySelector('.deck-main').addEventListener('touchend',e=>{if(!touch)return;const dx=e.changedTouches[0].clientX-touch[0],dy=e.changedTouches[0].clientY-touch[1];if(Math.abs(dx)>90&&Math.abs(dy)<50)show(index+(dx<0?1:-1),true);touch=null;},{passive:true});
    document.querySelector('.menu-toggle').addEventListener('click',e=>{const open=document.querySelector('.sidebar').classList.toggle('open');e.currentTarget.setAttribute('aria-expanded',String(open));});
  }
  document.querySelectorAll('.flip').forEach(b=>b.addEventListener('click',()=>{const open=b.getAttribute('aria-expanded')!=='true';b.setAttribute('aria-expanded',String(open));b.querySelector('.flip-front').setAttribute('aria-hidden',String(open));b.querySelector('.flip-back').setAttribute('aria-hidden',String(!open));}));
  document.querySelectorAll('.check-options').forEach(group=>group.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{group.querySelectorAll('button').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));const ok=b.dataset.correct==='true';group.nextElementSibling.textContent=(ok?'Correct. ':'Try again. ')+(ok?group.dataset.explanation:'Think about the task and choose another answer.');})));
  document.querySelectorAll('[data-print]').forEach(b=>b.addEventListener('click',()=>window.print()));
  document.querySelectorAll('.worksheet-input').forEach(t=>{t.addEventListener('input',()=>{t.nextElementSibling.textContent=t.value;t.style.height='auto';t.style.height=t.scrollHeight+'px';});});
  const form=document.querySelector('#practice-form');
  form?.addEventListener('submit',e=>{e.preventDefault();document.querySelector('#form-result').textContent=`Practice complete: ${form.elements.topic.value}; ${form.elements.method.value}. No request was sent. Review your choices or reset to try again.`;});
  form?.addEventListener('reset',()=>document.querySelector('#form-result').textContent='');
  const permission=document.querySelector('#permission');
  permission?.addEventListener('change',()=>{document.querySelector('#permission-result').textContent={viewer:'Viewer: Alex can read this fictional file. They cannot edit it.',commenter:'Commenter: Alex can suggest clearer wording. You decide which edits to make.',editor:'Editor: Alex can change the fictional file. Use this only for coauthoring.'}[permission.value]||'Choose a permission.';});
  const paper=document.querySelector('#paper-cost');
  paper?.addEventListener('input',()=>{const n=Number(paper.value);document.querySelector('#budget-total').textContent=paper.value!==''&&Number.isFinite(n)&&n>=0?`Total: $${(n+8+5).toFixed(2)}`:'Enter a nonnegative paper cost.';});
  document.querySelectorAll('[data-week-status]').forEach(el=>{const p=window.VubProgress?.get('dl2',el.dataset.weekStatus);el.textContent=p?.completed?'Lesson viewed to the end':p?`Resume at slide ${p.slide+1}`:'Ready to begin';});
})();
