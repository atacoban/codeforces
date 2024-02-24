c=[]
for i in range(int(input())):
    a=[*(input())]
    print(a)
    if (a[0]=='y' or a[0]=='Y') and (a[1]=='e' or a[1]=='E') and (a[2]=='s' or a[2]=='S'):
        c.append(True)
    else:
        c.append(False)

for i in c:
    if c:
        print('YES')
    else:
        print('NO')





