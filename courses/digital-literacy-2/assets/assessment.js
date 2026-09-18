(() => {
  'use strict';
  const form=document.querySelector('#assessment-form'), kind=form.dataset.kind;
  const key='vub:dl2:assessment:v1:'+kind;
  const box=document.querySelector('#questions'), error=document.querySelector('#assessment-error'), results=document.querySelector('#results');
  let questions=[], data={answers:{},learner:'',preScore:'',graded:false,index:0,review:false};
  const esc=s=>String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  function save(){try{sessionStorage.setItem(key,JSON.stringify(data));}catch(_){error.textContent='This browser cannot save the draft. You can still finish and print this page; keep it open until then.';}}
  function updateProgress(){
    const count=questions.filter(q=>Number.isInteger(data.answers[q.id])).length;
    document.querySelector('#answer-count').textContent=`${count} of ${questions.length||28} answered`;
    document.querySelector('#assessment-progress').value=count;
    document.querySelector('#grade').classList.toggle('ready',count===28);
    document.querySelectorAll('[data-topic-index]').forEach((button,i)=>{
      const group=questions.slice(i*4,i*4+4);button.querySelector('small').textContent=`${group.filter(q=>Number.isInteger(data.answers[q.id])).length} / 4 answered`;
      if(Math.floor(data.index/4)===i)button.setAttribute('aria-current','step');else button.removeAttribute('aria-current');
    });
  }
  function showQuestion(index,review=false,focus=true){
    data.index=Math.max(0,Math.min(questions.length-1,index));data.review=review;
    document.body.classList.toggle('review-mode',review);
    box.querySelectorAll('fieldset').forEach((field,i)=>{field.hidden=!review&&i!==data.index;});
    document.querySelector('#question-position').textContent=review?'Review your answers':`Question ${data.index+1} of ${questions.length}`;
    document.querySelector('#question-previous').disabled=data.index===0;
    document.querySelector('#question-next').disabled=data.index===questions.length-1;
    document.querySelector('#review-questions').textContent=review?'Return to focused view':'Review all questions';
    updateProgress();save();
    if(focus)document.querySelector('#group-'+questions[data.index].id)?.focus();
  }
  document.querySelector('#question-previous').addEventListener('click',()=>showQuestion(data.index-1));
  document.querySelector('#question-next').addEventListener('click',()=>showQuestion(data.index+1));
  document.querySelector('#review-questions').addEventListener('click',()=>showQuestion(data.index,!data.review));
  document.querySelector('#assessment-topics').addEventListener('click',event=>{
    const button=event.target.closest('[data-topic-index]');if(!button)return;
    const start=Number(button.dataset.topicIndex)*4;const missing=questions.slice(start,start+4).findIndex(q=>!Number.isInteger(data.answers[q.id]));
    showQuestion(start+(missing<0?0:missing));
  });
  function capture(){data.learner=form.elements.learner.value;data.preScore=form.elements.preScore?.value??'';questions.forEach(q=>{const checked=form.querySelector(`input[name="${q.id}"]:checked`);if(checked)data.answers[q.id]=Number(checked.value);});save();updateProgress();}
  function clear(){data={answers:{},learner:'',preScore:'',graded:false,index:0,review:false};try{sessionStorage.removeItem(key);}catch(_){} form.reset();form.querySelectorAll('input[type="radio"]').forEach(input=>{input.checked=false;input.defaultChecked=false;});form.elements.learner.value='';if(form.elements.preScore)form.elements.preScore.value='';results.hidden=true;results.replaceChildren();form.hidden=false;document.body.classList.remove('has-results');showQuestion(0,false,false);error.textContent='Assessment cleared. You may start again.';document.querySelector('#answer-count').textContent='0 of 28 answered';document.querySelector('.learner-details').open=true;form.elements.learner.focus();}
  function renderResults(){
    let score=0;const domains={};
    questions.forEach(q=>{domains[q.domain]??={score:0,total:0};domains[q.domain].total++;if(data.answers[q.id]===q.answer){score++;domains[q.domain].score++;}});
    const pct=Math.round(score/questions.length*100);
    let comparison='';
    if(kind==='post'&&data.preScore!=='') {const old=Number(data.preScore);if(Number.isInteger(old)&&old>=0&&old<=questions.length){const change=score-old,pp=Math.round(change/questions.length*100);comparison=`<p>Self-entered pre-test: ${old}/28. Change: ${change>0?'+':''}${change} points (${pp>0?'+':''}${pp} percentage points). Comparison assumes both scores belong to the same learner and the same assessment version.</p>`;}}
    const review=questions.map((q,i)=>{const correct=data.answers[q.id]===q.answer;return `<section class="result-item"><h3>${i+1}. ${esc(q.question)}</h3><p><strong>${correct?'Correct':'Review this topic'}</strong> · Your answer: ${esc(q.options[data.answers[q.id]])}</p>${correct?'':`<p>Correct answer: ${esc(q.options[q.answer])}</p>`}<p>${esc(q.why)}</p><p><a href="/courses/digital-literacy-2/weeks/week-${String(q.week).padStart(2,'0')}/presentation.html">Review week ${q.week}</a> · ${esc(q.domain)}</p></section>`;}).join('');
    results.innerHTML=`<h2 id="results-title" tabindex="-1">${kind==='pre'?'Pre-test':'Post-test'} graded results</h2><p>${data.learner?`Learner: ${esc(data.learner)} · `:''}Digital Literacy Level 2 · Assessment version 1</p><p class="score">${score} / ${questions.length} · ${pct}%</p><p>One point per correct answer. This classroom score guides practice; it is not an IC3 certification score.</p>${comparison}<div class="table-scroll"><table><caption>Results by domain</caption><thead><tr><th>Domain</th><th>Correct</th><th>Practice guidance</th></tr></thead><tbody>${Object.entries(domains).map(([d,v])=>`<tr><td>${esc(d)}</td><td>${v.score} / ${v.total}</td><td>${v.score===v.total?'Keep applying these skills':'Review explanations and repeat a related task'}</td></tr>`).join('')}</tbody></table></div><div class="actions"><button type="button" id="print-results">Print / Save as PDF</button><button type="button" class="secondary" id="download-results">Download results</button><button type="button" class="secondary" id="retake">Clear my assessment</button></div><p class="print-instructions">Choose Save as PDF in your browser’s print destination. Download results saves a standalone HTML copy that you can reopen and print later.</p><h2>Answers and explanations</h2>${review}`;
    form.hidden=true;results.hidden=false;document.body.classList.add('has-results');document.body.classList.remove('review-mode');
    document.querySelector('#print-results').addEventListener('click',()=>window.print());
    document.querySelector('#retake').addEventListener('click',clear);
    document.querySelector('#download-results').addEventListener('click',()=>{
      const copy=results.cloneNode(true);copy.querySelectorAll('.actions,.print-instructions').forEach(x=>x.remove());copy.querySelectorAll('a').forEach(a=>a.replaceWith(a.textContent));
      const content='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>VUB graded results</title><style>body{font:18px/1.6 system-ui;max-width:900px;margin:2rem auto;padding:1rem;color:#16243a}h1,h2,h3{line-height:1.3}table{border-collapse:collapse;width:100%}td,th{border:1px solid #777;padding:.5rem;text-align:left}.score{font-size:2rem;font-weight:bold}.result-item{border-bottom:1px solid #aaa;break-inside:avoid}@media print{body{font-size:12pt;margin:0}@page{margin:.6in}}</style><body><h1>VUB Learning</h1>'+copy.innerHTML+'</body></html>';
      const url=URL.createObjectURL(new Blob([content],{type:'text/html'}));const a=document.createElement('a');a.href=url;a.download='vub-level-2-'+kind+'-results.html';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
    });
    document.querySelector('#results-title').focus();
  }
  document.querySelector('#clear-assessment').addEventListener('click',clear);
  form.addEventListener('change',capture);form.addEventListener('input',capture);
  form.addEventListener('submit',event=>{event.preventDefault();capture();const missing=questions.find(q=>!Number.isInteger(data.answers[q.id]));if(missing){error.textContent='Please answer every question before grading. The first unanswered question is focused below.';showQuestion(questions.indexOf(missing));return;}const p=form.elements.preScore;if(p&&p.value!==''&&(!Number.isInteger(Number(p.value))||Number(p.value)<0||Number(p.value)>28)){error.textContent='Enter a whole-number pre-test score from 0 to 28, or leave it blank.';document.querySelector('.learner-details').open=true;p.focus();return;}error.textContent='';data.graded=true;save();renderResults();});
  async function load(){try{
    const response=await fetch('/courses/digital-literacy-2/assets/questions.json');if(!response.ok)throw new Error('Question file unavailable');const bank=await response.json();questions=bank[kind];if(!Array.isArray(questions)||questions.length!==28)throw new Error('Invalid question bank');
    try{const parsed=JSON.parse(sessionStorage.getItem(key)||'null');if(parsed&&typeof parsed.answers==='object'&&parsed.answers!==null){data={answers:{},learner:typeof parsed.learner==='string'?parsed.learner.slice(0,80):'',preScore:typeof parsed.preScore==='string'?parsed.preScore:'',graded:parsed.graded===true,index:Number.isInteger(parsed.index)&&parsed.index>=0&&parsed.index<28?parsed.index:0,review:parsed.review===true};questions.forEach(q=>{if(Number.isInteger(parsed.answers[q.id])&&parsed.answers[q.id]>=0&&parsed.answers[q.id]<q.options.length)data.answers[q.id]=parsed.answers[q.id];});}}catch(_){}
    const short=['Technology','Citizenship','Information','Creating','Communication','Collaboration','Safety'];
    document.querySelector('#assessment-topics').innerHTML=questions.filter((_,i)=>i%4===0).map((q,i)=>`<button type="button" data-topic-index="${i}" aria-label="${esc(q.domain)}"><span class="topic-number">${i+1}</span><span>${short[i]}<small>0 / 4 answered</small></span></button>`).join('');
    box.innerHTML=questions.map((q,i)=>`<fieldset id="group-${q.id}" tabindex="-1"><legend><span class="visually-hidden">${esc(q.domain)}</span>${i+1}. ${esc(q.question)}</legend>${q.options.map((o,j)=>`<label><input type="radio" name="${q.id}" value="${j}" ${data.answers[q.id]===j?'checked':''}> <span>${esc(o)}</span></label>`).join('')}</fieldset>`).join('');
    form.elements.learner.value=data.learner;if(form.elements.preScore)form.elements.preScore.value=data.preScore;
    document.querySelector('#grade').disabled=false;document.querySelector('#review-questions').disabled=false;
    showQuestion(data.index,data.review,false);
    if(data.graded&&Object.keys(data.answers).length===questions.length)renderResults();

  }catch(_){box.innerHTML='<p>Questions could not load. Check your connection and reload this page, or use the printable paper assessment.</p>';error.textContent='Automatic grading is unavailable until all questions load.';}}
  load();
})();
