import sub2.calc 
import sub2.calc as c #sub2.calc 다 치기 귀찮아서 as c 로 별칭
from sub2.calc import *


r1 = sub2.calc.plus(1, 2)
print('r1 :', r1)

r2 = c.plus(1, 2)
print('r2 :', r2)

r3 = multi(3, 4)
print('r3 :', r3)

r4 = div(4, 2)
print('r4 :', r4)