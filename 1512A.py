c=[]
for i in range(int(input())):
    
    input()
    a=list(map(int,input().split())) 
    for index, value in enumerate(a):
        if index==0:
            if value!=a[1] and value !=a[2]:
                c.append(index+1)
                break
        elif value==a[0]:
            continue
        else:
            c.append(index+1)
for i in range(len(c)):
    print(c[i])
        













