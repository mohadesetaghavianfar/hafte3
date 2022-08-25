import _random
from math import radians
import random
from tokenize import Number

AdadRandom=0

num=[]
pow_num=[]


for i in range (0 , 20):
    Number=random.randint(0 , 200)
    num.append(Number)
    if len(num)==20:
        break

print('numbers is:\n' , num)
for i in num:
    pow_num.append(i**2)
print('pow_num ps:\n' , pow_num)

