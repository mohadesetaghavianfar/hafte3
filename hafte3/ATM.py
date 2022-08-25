password=1869
counter=0

i=1

while i<4:
    x = int(input('please enter your password:\n'))
    R = int(x/1000)
    if 0 < R <10:
       if x==9681:
         print('WRONG! WE WILL CALL THE POLICE.')
       elif x==password:
        print('PASSWORD IS TRUE.')
        break
       else:
        print('YOUR PASSWORD IS WRONG!')
        i=i+1
    else:
        continue
if i>3:
    print('YOUR ACCOUNT IS LOCKED!')