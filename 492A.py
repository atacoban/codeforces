num=int(input())
a=0
b=1
i=2
count=0
if num==1:
    print(1)
elif num==0:
    print(0)
else:
    while a<num:
        a+=b
        count+=1
        b+=i
        i+=1
    if a==num:
        print(count)
    else:
        print(count-1)
