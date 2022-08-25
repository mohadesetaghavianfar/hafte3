import random
from tkinter import N

sum=0

while True:
    start = input('start?(Y/N) :').upper
    
    if start=='Y':
        dice=random.randint(1 , 6)
        if dice==6:
            print(dice)
            sum=sum+dice
            continue
        else:
            sum=sum+dice
            N
            print('sum is:' , sum)
            break
    if start=='N':
        print('your program is closed!')
    