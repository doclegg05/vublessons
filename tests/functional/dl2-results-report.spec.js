const {test,expect}=require('@playwright/test');const AxeBuilder=require('@axe-core/playwright').default;const fs=require('fs');const bank=require('../../courses/digital-literacy-2/assets/questions.json');
async function result(page,kind,score,preScore=''){
 await page.goto(`/courses/digital-literacy-2/assessments/${kind}-test.html`);
 await page.evaluate(({kind,score,preScore,bank})=>sessionStorage.setItem(`vub:dl2:assessment:v${kind==='post'?3:2}:${kind}`,JSON.stringify({answers:Object.fromEntries(bank[kind].map((q,i)=>[q.id,i<score?q.answer:(q.answer+1)%q.options.length])),learner:'Sample <learner>',preScore,graded:true,index:0,review:false})),{kind,score,preScore,bank});await page.reload();await expect(page.locator('#results-title')).toBeVisible();
}
for(const kind of ['pre','post'])test(`DL2 ${kind} branded results stay accessible and preserve an offline printable report`,async({page,browser})=>{
 await result(page,kind,kind==='pre'?0:14,kind==='post'?'20':'');
 await expect(page.locator('.report-version')).toContainText(`Assessment version ${kind==='post'?3:2}`);
 await expect(page.locator('.report-masthead')).toContainText('Veterans Upward Bound');await expect(page.locator('.practice-plan li')).toHaveCount(2);await expect(page.locator('.domain-table tbody tr')).toHaveCount(7);await expect(page.locator('.report-learner')).toHaveText('Learner: Sample <learner>');
 if(kind==='post')await expect(page.locator('.report-comparison')).toContainText('-6 points (-21 percentage points)');
 const scan=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();expect(scan.violations.map(v=>({id:v.id,targets:v.nodes.map(n=>n.target)}))).toEqual([]);
 await page.setViewportSize({width:390,height:844});for(let i=0;i<3;i++)await page.getByRole('button',{name:'Increase text size'}).click();expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1)).toBeTruthy();
 await page.emulateMedia({media:'print'});await expect(page.locator('.report-masthead strong')).toHaveCSS('color','rgb(255, 255, 255)');await expect(page.locator('.actions').first()).toBeHidden();await expect(page.locator('.report-overview')).toHaveCSS('break-after','page');await page.emulateMedia({media:'screen'});
 const pending=page.waitForEvent('download');await page.getByRole('button',{name:'Download results',exact:true}).click();const download=await pending;const html=fs.readFileSync(await download.path(),'utf8');expect(html).not.toContain('<script');expect(html).toContain('data:image/png;base64,');
 const offline=await browser.newPage();const requests=[];await offline.route('**/*',route=>{requests.push(route.request().url());route.abort()});await offline.setContent(html);await expect(offline.locator('.report-masthead')).toHaveCSS('background-color','rgb(27, 54, 93)');await expect(offline.locator('.result-item')).toHaveCount(28);expect(await offline.locator('img').evaluate(i=>i.complete&&i.naturalWidth>0)).toBeTruthy();expect(requests).toEqual([]);await offline.emulateMedia({media:'print'});await expect(offline.locator('.report-masthead strong')).toHaveCSS('color','rgb(255, 255, 255)');await offline.close();
});
test('DL2 perfect results offer application practice without invented weak domains',async({page})=>{
 await result(page,'post',28,'28');await expect(page.locator('.practice-plan')).toContainText('answered every item correctly');await expect(page.locator('.practice-plan li')).toHaveCount(0);await expect(page.locator('.report-comparison')).toContainText('Change: 0 points (0 percentage points)');await expect(page.locator('.needs-practice')).toHaveCount(0);
});
for(const kind of ['pre','post'])test(`DL2 ${kind} scenario questions and paper answer key stay aligned`,async({page})=>{
 await page.goto(`/courses/digital-literacy-2/assessments/${kind}-test-printable.html`);
 await expect(page.locator('main')).toContainText(`Assessment version ${kind==='post'?3:2}`);
 const paper=page.locator('section.question');await expect(paper).toHaveCount(28);
 for(const [i,q] of bank[kind].entries()){
  await expect(paper.nth(i).locator('h2')).toHaveText(`${i+1}. ${q.question}`);
  expect(await paper.nth(i).locator('li').allTextContents()).toEqual(q.options.map(o=>'☐ '+o));
 }
 await page.goto(`/courses/digital-literacy-2/assessments/${kind}-test-answer-key.html`);
 const key=page.locator('section.question');await expect(key).toHaveCount(28);
 for(const [i,q] of bank[kind].entries()){
  await expect(key.nth(i).locator('h2')).toHaveText(`${i+1}. ${q.question}`);
  await expect(key.nth(i).locator('strong')).toHaveText(`${'ABC'[q.answer]}. ${q.options[q.answer]}`);
  await expect(key.nth(i)).toContainText(q.why);
 }
});
test('DL2 revised scenarios do not reuse version 1 draft answers or graded results',async({page})=>{
 await page.goto('/courses/digital-literacy-2/assessments/pre-test.html');
 await page.evaluate(bank=>sessionStorage.setItem('vub:dl2:assessment:v1:pre',JSON.stringify({answers:Object.fromEntries(bank.pre.map(q=>[q.id,q.answer])),learner:'Old draft',graded:true,index:27})),bank);
 await page.reload();await expect(page.locator('fieldset')).toHaveCount(28);
 await expect(page.locator('#results')).toBeHidden();await expect(page.locator('input:checked')).toHaveCount(0);
 await expect(page.locator('#question-position')).toHaveText('Question 1 of 28');
 await page.locator('input[name="pre-01"]').first().check();await page.reload();
 await expect(page.locator('input:checked')).toHaveCount(1);
 expect(await page.evaluate(()=>JSON.parse(sessionStorage.getItem('vub:dl2:assessment:v1:pre')).learner)).toBe('Old draft');
});
test('DL2 new post-test preserves the existing pre-test and ignores old post answers',async({page})=>{
 await page.goto('/courses/digital-literacy-2/assessments/post-test.html');
 await page.evaluate(bank=>{
  for(const kind of ['pre','post'])sessionStorage.setItem('vub:dl2:assessment:v2:'+kind,JSON.stringify({answers:Object.fromEntries(bank[kind].map(q=>[q.id,q.answer])),learner:'Saved learner',graded:true,index:0,preScore:''}));
 },bank);
 await page.reload();await expect(page.locator('fieldset')).toHaveCount(28);
 await expect(page.locator('#results')).toBeHidden();await expect(page.locator('input:checked')).toHaveCount(0);
 await expect(page.locator('main')).toContainText('Assessment version 3');
 await page.locator('input[name="post-01"]').first().check();await page.reload();await expect(page.locator('input:checked')).toHaveCount(1);
 await page.goto('/courses/digital-literacy-2/assessments/pre-test.html');
 await expect(page.locator('.score')).toHaveText('28 / 28 · 100%');await expect(page.locator('.report-version')).toContainText('Assessment version 2');
 expect(await page.evaluate(()=>JSON.parse(sessionStorage.getItem('vub:dl2:assessment:v2:post')).learner)).toBe('Saved learner');
});
