s=input()
a="hello"
x=0
for i in s:
    if i==a[x]:
        x+=1
        if x==5:
            print('YES')
            break
if x<5:
    print('NO')

    
    


