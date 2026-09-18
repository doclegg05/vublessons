/* All examples are local models: no device settings, permissions or accounts change. */
(() => {
  'use strict';
  // Reserve space for the shared text-size control instead of overlaying examples.
  const dockTextSize = () => {
    const control=document.querySelector('.vub-textsize-fab');
    const toolbar=document.querySelector('.deck-toolbar');
    if(control&&toolbar){toolbar.append(control);return true;}return false;
  };
  if(document.body.classList.contains('lesson')&&!dockTextSize()){
    const observer=new MutationObserver(()=>{if(document.querySelector('.vub-textsize-fab')){observer.disconnect();dockTextSize();}});
    observer.observe(document.body,{childList:true});
  }
  const resources = ['Community library · Learning','Computer help desk · Learning','Neighborhood center · Community'];
  const say = (root,text) => { root.querySelector('.work-outcome').textContent=text; };
  const filter = root => {
    const query=root.querySelector('[data-resource-search]').value.trim().toLowerCase();
    const matches=resources.filter(x=>x.toLowerCase().includes(query));
    const target=root.querySelector('.resource-results');target.replaceChildren();
    matches.forEach(text=>{const row=document.createElement('div');row.className='result-row';row.textContent=text;target.append(row);});
    if(!matches.length)target.textContent='No matching resources. Try another word or reset your search.';
    say(root,`${matches.length} fictional resource${matches.length===1?'':'s'} found. ${query?'Compare the result with what you expected.':'All resources are visible.'}`);
  };
  document.querySelectorAll('[data-workshop]').forEach(root=>{
    const initial={zoom:'100',output:'headphones',calendar:'week',privacy:'busy',document:'plain',export:'doc',feedback:'vague',encrypt:'plain',parts:'html'};
    Object.entries(initial).forEach(([a,v])=>root.querySelector(`button[data-action="${a}"][data-value="${v}"]`)?.setAttribute('aria-pressed','true'));
    root.querySelector('.calendar-surface')?.addEventListener('keydown',event=>{
      if(['ArrowLeft','ArrowRight','Home','End'].includes(event.key)){event.preventDefault();event.stopPropagation();const pane=event.currentTarget;pane.scrollLeft=event.key==='Home'?0:event.key==='End'?pane.scrollWidth:pane.scrollLeft+(event.key==='ArrowRight'?160:-160);}
    });
    root.querySelector('[data-resource-search]')?.addEventListener('input',()=>filter(root));
    root.addEventListener('click',event=>{
      const b=event.target.closest('button[data-action]');if(!b)return;
      const a=b.dataset.action,v=b.dataset.value;
      const q=selector=>root.querySelector(selector);
      if(b.hasAttribute('aria-pressed')&&!['mute','meeting-mic','hand'].includes(a))root.querySelectorAll(`button[data-action="${a}"]`).forEach(x=>x.setAttribute('aria-pressed',String(x===b)));
      if(a==='zoom'){q('.zoom-page').style.setProperty('--demo-zoom',Number(v)/100);say(root,`Page zoom: ${v}%. The surrounding controls have not changed. Check that the text and example link still fit.`);}
      if(a==='output'){q('[data-output]').textContent=v==='speakers'?'Speakers':'Headphones';root.dataset.output=v;root.classList.remove('sound-running');say(root,`${q('[data-output]').textContent} selected. Run a visual sound test to check the selected route.`);}
      if(a==='mute'){const muted=b.getAttribute('aria-pressed')!=='true';b.setAttribute('aria-pressed',String(muted));b.textContent=`Mute: ${muted?'on':'off'}`;root.dataset.muted=String(muted);root.classList.remove('sound-running');say(root,muted?'Muted. A correct output still cannot play while muted.':'Mute is off. Now check the selected output.');}
      if(a==='sound-test'){const muted=root.dataset.muted==='true';root.classList.toggle('sound-running',!muted);say(root,muted?'No output: the model is muted. Turn mute off, then test again.':`Visual test reaches ${q('[data-output]').textContent.toLowerCase()}. On your real computer, play a short sound to verify.`);}
      if(a==='calendar'){q('.calendar-surface').dataset.view=v;say(root,v==='day'?'Day view: Monday only, with room for its details.':v==='month'?'Month view: the same plans within a fictional 28-day overview. Scroll sideways on a narrow screen.':v==='list'?'List view: read just the events, without the empty calendar space.':'Week view: compare plans across three practice days.');}
      if(a==='privacy'){q('[data-shared-event]').replaceChildren();const title=document.createTextNode(v==='busy'?'Busy':'Practice appointment');const line=document.createElement('span');line.textContent=v==='busy'?'2:00–3:00':'2:00–3:00 · Room A';q('[data-shared-event]').append(title,line);say(root,v==='busy'?'Your partner sees availability. The title and location remain private in this model.':'Your partner can now see the title and location. Share this only when the task requires it.');}
      if(a==='sync'){const deleted=v==='delete';root.querySelectorAll('[data-local-file],[data-cloud-file]').forEach(x=>{x.textContent=deleted?'File deleted':'Resource guide.docx';x.classList.toggle('deleted',deleted);});say(root,deleted?'Deletion synced to both locations. The separate backup still holds an earlier recovery copy.':v==='restore'?'Restored from the separate backup. Check its version before relying on it.':'Reset: the file is present in both synced locations and in the separate backup.');}
      if(a==='source')say(root,{author:'An identified author is a starting point. Check their expertise and whether the organization is real.',date:'Look for an update date and verify that the service still operates. An undated result needs another check.',purpose:'A page may inform, sell or persuade. Compare its claim with an independent source.'}[v]);
      if(a==='document'){q('[data-document]').classList.toggle('structured',v==='structured');say(root,v==='structured'?'The modeled heading is distinct and the three steps have an order. In your editor, apply a real heading style—not just bold text.':'All lines look alike. A reader has to work harder to find the task and its steps.');}
      if(a==='sheet'){q('[data-paper]').textContent=`$${v}`;q('[data-sum]').textContent=`$${Number(v)+13}`;say(root,`Paper $${v} + folders $8 + pens $5 = $${Number(v)+13}. The total includes all three cells.`);}
      if(a==='export'){const data={doc:['DOCX','Keep revising together','Preserve editable text and document structure in a compatible app.'],pdf:['PDF','Share a finished layout','Check the exported pages, text and links before sending.'],csv:['CSV','Move plain table data','Formatting and formulas are not preserved. Reopen the file and check values.']}[v];['[data-extension]','[data-export-title]','[data-export-copy]'].forEach((s,i)=>q(s).textContent=data[i]);say(root,`${data[0]} selected. Reopen the exported file to check what survived.`);}
      if(a==='feedback'){q('[data-comment]').textContent={vague:'This is confusing.',specific:'After step 2, add the contact number so readers can find help.',resolved:'Writer: I added the contact number after step 2. Please check the revised handout.'}[v];say(root,v==='vague'?'The writer cannot tell where to make a change.':v==='specific'?'Location: after step 2. Change: add the contact number. Reason: readers can find help.':'The writer names the change and asks for a check. Resolving a comment should follow the actual revision.');}
      if(a==='meeting-mic'){const on=b.getAttribute('aria-pressed')!=='true';b.setAttribute('aria-pressed',String(on));b.textContent=on?'Mute microphone':'Unmute microphone';q('[data-mic-state]').textContent=on?'Microphone on (model)':'Microphone muted';say(root,on?'The model microphone is on. Mute when appropriate to avoid background noise.':'The model microphone is muted. No real device permission was requested.');}
      if(a==='hand'){const raised=b.getAttribute('aria-pressed')!=='true';b.setAttribute('aria-pressed',String(raised));b.textContent=raised?'Lower hand':'Raise hand';say(root,raised?'Hand raised in the model. Wait for the host to invite you to speak.':'Hand lowered. Follow the host’s instructions.');}
      if(a==='inspect'){say(root,{urgency:'Pressure signal: a deadline can push you to skip checks. Urgency is a reason to pause, not proof by itself.',sender:'Check the full sender address. A familiar display name can hide a different domain. This .example address is fictional.',link:'The fictional destination is account-check.example/verify. Use a known website or contact method instead of the message link.',verify:'Safer next step: open a known official website yourself or call a verified number, then check the claim.'}[v]);b.classList.add('inspected');}
      if(a==='access')say(root,v==='deny'?'Good fit: a text-only page does not need your camera for this task. Deny unrelated access.':'Reconsider: this task does not explain a need for camera access. Deny it and verify the app’s purpose.');
      if(a==='encrypt'){q('[data-protection]').textContent={plain:'Original file',readonly:'Read-only file',encrypted:'Encrypted file'}[v];q('[data-file-text]').textContent=v==='encrypted'?'7fA2 · 9cD4 · e18B\nUnreadable without the key':'Practice notes\nResource desk · Room A';q('[data-protection-note]').textContent={plain:'Readable and editable.',readonly:'Still readable. Editing is restricted.',encrypted:'Illustrative ciphertext. The key is required to recover readable data.'}[v];say(root,v==='readonly'?'Read-only limits changes; it does not make the content secret.':v==='encrypted'?'Encryption protects readability without a key. It is different from limiting edits.':'Start with readable data, then compare the two protections.');}
      if(a==='parts'){q('[data-code]').textContent={html:'<h1>Find a resource</h1>\n<input aria-label="Search">',css:'.result {\n  padding: 1rem;\n  color: #1B365D;\n}',js:'resources.filter(item =>\n  item.name.includes(query)\n)'}[v];q('.mini-app').dataset.layer=v;say(root,{html:'HTML names the content and controls. It provides the structure.',css:'CSS changes the visual layout and appearance. It does not create a secure account system.',js:'JavaScript responds to input. Here it can filter the fictional records.'}[v]);}
      if(a==='app'){q('[data-resource-search]').value=v;filter(root);}
      if(a==='prompt'){const task=q('[data-prompt-task]').value.trim();if(!task){say(root,'Enter the task your fictional app should help someone complete.');q('[data-prompt-task]').focus();return;}const requirements=[...root.querySelectorAll('[data-requirement]:checked')].map(x=>x.dataset.requirement);q('[data-prompt-output]').textContent=`Build a one-page app to help someone ${task.charAt(0).toLowerCase()+task.slice(1)}.\n${requirements.join('\n')}\nUse fictional data and no external dependencies. Do not include secrets, payments or a real account system. Explain the code and give me observable tests.`;say(root,'Practice prompt built locally. Read it, refine it, and decide how you will test each requirement.');}
    });
  });
})();
