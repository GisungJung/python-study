import calc
from calc import sum

print(calc.sum(1, 2)) # 3
print(sum(1, 2)) # 3

# PYTHONPATH 환경변수 설정 고려 
import calculate.say.hello

import calculate.say.talk as talk
talk.talk('Hello Wold')

from calculate.calc.multi import multi
print(multi(3, 4))

from calculate.calc import *
print(multi.multi(2, 4))
print(sum.sum(1, 3))
            
