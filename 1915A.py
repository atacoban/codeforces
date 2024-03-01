d=[]
for i in range(int(input())):
    a,b,c=input().split()
    if a==b:
        d.append(c)
    elif a==c:
        d.append(b)
    else:
        d.append(a)
for i in d:
    print(i)
