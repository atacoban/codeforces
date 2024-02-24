"""k=int(input())
a=list(map(int,input().split()))
b=0
c=0
d=0
f=len(a)-1
if k%2==1:
    k+=1
    for i in range(k//2):
        if a[d]>a[f]:
            b+=a[d]
            d+=1
        else:
            b+=a[f]
            f-=1
        if a[d]>a[f]:
            c+=a[d]
            d+=1
        else:
            c+=a[f]
            f-=1
    if a[0]>a[-1]:
        c=c-a[0]
    else:
        c=c-a[-1]
else:
    for i in range(k//2):
        if a[d]>a[f]:
            b+=a[d]
            d+=1
        else:
            b+=a[f]
            f-=1
        if a[d]>a[f]:
            c+=a[d]
            d+=1
        else:
            c+=a[f]
            f-=1
print(b,c)"""    



k=int(input())
a=list(map(int,input().split()))
b=True
e=0
f=len(a)-1
p1=0
p2=0
while e-1!=f:
    if b==True:
        if a[e]>a[f]:
            p1+=a[e]
            e+=1
            b=False
        else:
            p1+=a[f]
            f-=1
            b=False
    else:
        if a[e]>a[f]:
            p2+=a[e]
            e+=1
            b=True
        else:
            p2+=a[f]
            f-=1
            b=True
print(p1,p2)
    















