(() => {
 'use strict';
 document.querySelector('.app-menu')?.addEventListener('click',event=>{const rail=event.currentTarget.closest('.app-rail');const open=rail.classList.toggle('menu-open');event.currentTarget.setAttribute('aria-expanded',String(open));});
 const path=location.pathname.replace(/\.html$/,'').replace(/\/$/,'');
 document.querySelectorAll('[data-app-route]').forEach(a=>{const u=new URL(a.href);if(!u.hash&&u.pathname.replace(/\.html$/,'').replace(/\/$/,'')===path)a.setAttribute('aria-current','page');});
 const dock=()=>{const slot=document.querySelector('[data-text-dock]'),control=document.querySelector('.vub-textsize-fab');if(slot&&control){slot.append(control);return true;}return false;};
 if(document.querySelector('[data-text-dock]')&&!dock()){const observer=new MutationObserver(()=>{if(dock())observer.disconnect();});observer.observe(document.body,{childList:true});}
 if(document.querySelector('.learning-home')){
  const p=window.VubProgress?.getCourseSummary('dl2');
  if(p){document.querySelector('[data-course-count]').textContent=`${p.completed} of 6 lessons viewed to the end`;document.querySelector('[data-course-progress]').value=p.completed;
   if(p.lastWeek&&Number(p.lastWeek)>=1&&Number(p.lastWeek)<=6){const n=Number(p.lastWeek),state=window.VubProgress.get('dl2',n),a=document.querySelector('.continue-course');a.href=`/courses/digital-literacy-2/weeks/week-${String(n).padStart(2,'0')}/presentation.html`;a.textContent=`Continue week ${n}`;document.querySelector('[data-continue-caption]').textContent=`Your place is saved: week ${n}, slide ${(state?.slide||0)+1}.`;}
  }
 }
})();

// Chapter controls seek within the learner-controlled video without autoplay.
(() => {
 document.querySelectorAll('[data-video-chapters]').forEach(nav=>{
  const video=document.getElementById(nav.dataset.videoChapters);
  if(!video)return;
  nav.querySelectorAll('[data-video-seek]').forEach(button=>button.addEventListener('click',()=>{
   const seek=()=>{video.currentTime=Number(button.dataset.videoSeek);video.pause();video.focus();};
   if(video.readyState>=1)seek();else{video.addEventListener('loadedmetadata',seek,{once:true});video.load();}
   nav.querySelectorAll('button').forEach(b=>b.removeAttribute('aria-current'));
   button.setAttribute('aria-current','true');
  }));
 });
})();
