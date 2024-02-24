a=int(input())
x=1
y=1
count=2
if a<=2:
    print(1)
else:
    while(True):
        y=x+y
        count+=1
        if count==a:
            print(y)
            break
        x=x+y
        count+=1
        if count==a:
            print(x)
            break







