k=[]
for i in range(int(input())):
    a,b,c=(map(int,input().split()))
    if max(a,b,c)==b:
        d=b-max(a,c)
        if (b+d)%a==0:
            k.append("Yes")
        else:
            k.append("No")
    elif ((a+c)/2)%b==0:
        k.append("Yes")
    else:
        k.append("No")

for i in k:
    print(i)
