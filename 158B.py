a=int(input())
b=list(map(int,input().split()))
i1=0
i2=0
i3=0
i4=0
for i in b:
    if i==1:
        i1+=1
    elif i==2:
        i2+=1
    elif i==3:
        i3+=1
    else:
        i4+=1
count=0

count+=i4
count+=i3
if i3<i1:
    i1=i1-i3
else:
    i1=0

k=i2//2
count+=k
i2=i2-((i2//2)*2)
if i1>=2 and i2==1:
    i2=0
    i1-=2
    count+=1

if i1==0:
    count+=i2

if i1%4==0:
    count+=i1//4
else:
    count+=(i1//4)+1
print(int(count))













