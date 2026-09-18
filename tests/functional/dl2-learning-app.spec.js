const {test,expect}=require('@playwright/test');
const AxeBuilder=require('@axe-core/playwright').default;
const base='/courses/digital-literacy-2';
test('DL2 focused assessment retains answers, position and truthful topic progress',async({page})=>{
 await page.goto(base+'/assessments/pre-test.html');await expect(page.locator('fieldset:visible')).toHaveCount(1);await expect(page.locator('#question-position')).toHaveText('Question 1 of 28');
 await page.locator('fieldset:visible input').first().check();await expect(page.locator('#answer-count')).toHaveText('1 of 28 answered');await expect(page.locator('[data-topic-index="0"] small')).toHaveText('1 / 4 answered');
 await page.getByRole('button',{name:'Next question',exact:true}).click();await expect(page.locator('#question-position')).toHaveText('Question 2 of 28');await page.locator('fieldset:visible input').last().check();
 await page.locator('[data-topic-index="6"]').focus();await page.keyboard.press('Enter');await expect(page.locator('#question-position')).toHaveText('Question 25 of 28');await page.reload();await expect(page.locator('#question-position')).toHaveText('Question 25 of 28');await expect(page.locator('#answer-count')).toHaveText('2 of 28 answered');
 await page.getByRole('button',{name:'Review all questions',exact:true}).click();await expect(page.locator('fieldset:visible')).toHaveCount(28);await page.getByRole('button',{name:'Grade my assessment',exact:true}).click();await expect(page.locator('#question-position')).toHaveText('Question 3 of 28');await expect(page.locator('fieldset:visible')).toBeFocused();
 await page.getByRole('button',{name:'Clear my assessment',exact:true}).click();await expect(page.locator('#assessment-progress')).toHaveAttribute('value','0');await expect(page.locator('[data-topic-index="0"] small')).toHaveText('0 / 4 answered');await page.reload();await expect(page.locator('#question-position')).toHaveText('Question 1 of 28');await expect(page.locator('input:checked')).toHaveCount(0);
});
test('DL2 course continue reflects the saved lesson rather than invented completion',async({page})=>{
 await page.goto(base+'/weeks/week-02/presentation.html');await page.locator('#next').click();await page.goto(base+'/index.html');await expect(page.locator('.continue-course')).toHaveText('Continue week 2');await expect(page.locator('[data-continue-caption]')).toContainText('slide 2');await expect(page.locator('[data-course-count]')).toHaveText('0 of 6 lessons viewed to the end');await page.locator('.continue-course').click();await expect(page.locator('#slide-counter')).toContainText('Slide 2');
});
test('DL2 learning app remains accessible on mobile with enlarged text and a selected answer',async({page})=>{
 await page.setViewportSize({width:390,height:844});await page.emulateMedia({reducedMotion:'reduce'});await page.goto(base+'/assessments/post-test.html');await page.getByRole('button',{name:'Course navigation',exact:true}).click();await expect(page.locator('#course-links')).toBeVisible();await page.getByRole('button',{name:'Course navigation',exact:true}).click();await expect(page.locator('#course-links')).toBeHidden();
 for(let i=0;i<3;i++)await page.getByRole('button',{name:'Increase text size'}).click();await page.locator('fieldset:visible input').first().check();expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth+1)).toBeTruthy();await expect(page.locator('.rail-bottom .vub-textsize-fab')).toHaveCSS('position','static');
 const result=await new AxeBuilder({page}).withTags(['wcag2a','wcag2aa','wcag21aa']).analyze();expect(result.violations.map(x=>({id:x.id,nodes:x.nodes.map(n=>n.target)}))).toEqual([]);
});
