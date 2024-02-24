c=[]
f=0
b=0
d=0
for i in range(int(input())):
    a=list(map(int,input().split()))  
    f+=a[0]
    b+=a[1]
    d+=a[2]

if b==0 and f==0 and d==0:
    print("YES")
else:
    print("NO")