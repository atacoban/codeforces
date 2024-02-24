c=[]
b=False
for i in range(int(input())):
    input()
    a=list(map(int,input().split()))   
    a.sort() 
    if len(a)==1:
        b=False
        c.append(b)
    elif a[0]+1<a[-1]:
        b=True
        c.append(b)       
    else:      
        b=False
        c.append(b)


for i in c:
    if i:
        print('NO')
    else:
        print('YES')









