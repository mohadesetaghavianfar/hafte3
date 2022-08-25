import random
i=0
answer=55
counter=0
while i==0:
    guess=random.randint(0,99)
    print(guess)
    while True:
        if guess==answer:
            print('yes, your guess is correct.')
            i=i+1
        elif guess > answer:
            print('is bigger!')
        elif guess<answer:
            print('is smaller!')
        break