g=[]
for i in range(int(input())):
    count=0
    a=list(map(int,input().split())) 
    b=a[0]
    a.sort()
    for i in a:
        if i>b:
            count+=1
        else:
            continue
    g.append(count)
for i in g:
    print(i)








