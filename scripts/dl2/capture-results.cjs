const {chromium}=require(process.cwd()+'/node_modules/@playwright/test');const fs=require('fs');const bank=require(process.cwd()+'/courses/digital-literacy-2/assets/questions.json');
(async()=>{const b=await chromium.launch();const out='docs/digital-literacy-2/review/results-report';fs.mkdirSync(out,{recursive:true});
for(const kind of ['pre','post']){
 const p=await b.newPage({viewport:{width:1440,height:1080}});await p.goto(`http://localhost:3940/courses/digital-literacy-2/assessments/${kind}-test.html`);
 await p.evaluate(({kind,bank})=>sessionStorage.setItem('vub:dl2:assessment:v1:'+kind,JSON.stringify({answers:Object.fromEntries(bank[kind].map((q,i)=>[q.id,i<(kind==='pre'?10:22)?q.answer:(q.answer+1)%q.options.length])),learner:'Sample learner',preScore:kind==='post'?'10':'',graded:true,index:0,review:false})),{kind,bank});await p.reload();await p.waitForSelector('#results-title');await p.evaluate(()=>document.fonts.ready);
 await p.screenshot({path:`${out}/${kind}-desktop.png`,fullPage:true});await p.pdf({path:`${out}/${kind}-report.pdf`,printBackground:true});
 await p.setViewportSize({width:390,height:844});await p.screenshot({path:`${out}/${kind}-mobile.png`,fullPage:true});await p.close();
}await b.close();})();
