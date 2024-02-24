c=[]
for i in range(int(input())):
    a=list(map(int,input().split()))   
    a.sort() 
    if a[0]+a[1]==a[2]:
        c.append(True)
    else:
        c.append(False)

for i in c:
    if i:
        print('YES')
    else:
        print('NO')




