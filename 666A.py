a=list(map(str,*(input().split())))
b=[]
count=0
if a[0]=='-':
    b.append(a[0])
    a.remove(a[0])
    count+=1
a.reverse()
for i in range(len(a)):
    if a[0]=="0":
        a.remove(a[0])
for i in a:
    b.append(int(i))
for i in b:
    print(i,end="")














