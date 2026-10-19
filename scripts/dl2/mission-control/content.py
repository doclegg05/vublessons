"""Mission Control weeks 2–6. Authored teaching sequence, not assessment data."""
def mission(title,app,start,finish,tell,show,do,question,choices,answer,why,lab,practice):
 return dict(title=title,app=app,start=start,finish=finish,tell=tell,show=show,do=do,question=question,choices=choices,answer=answer,why=why,lab=lab,practice=practice)
from week2 import WEEK2
from week3 import WEEK3
from week4 import WEEK4
from week5 import WEEK5
from week6 import WEEK6
WEEKS={
2:WEEK2,
3:WEEK3,
4:WEEK4,
5:WEEK5,
6:WEEK6,
}
