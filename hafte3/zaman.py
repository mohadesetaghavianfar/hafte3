time=int(input('choose:\n1)hour to second\t2)second to hour\n'))
if time==1:
    while True:
        second=int(input('enter your second:\n'))
        hour=int(input('enter your hour:\n'))
        minute=int(input('enter your minute:\n'))
        if(second<60) & (hour<24) & (minute<60):
            hour=hour*3600
            minute=minute*60
            sum=hour+minute
            print(sum,'second')
            break
        else:
            continue
elif time==2:
    convertTolnt=int(input('enter your second:\n'))
    hour=int(convertTolnt/3600)
    minute=((convertTolnt%3600)/60)
    second=float(minute%60)
    print(hour, minute,second)
   
