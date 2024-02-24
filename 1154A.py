a=list(map(int,input().split()))
m=max(a)
for i in a:
    if i==m:
        continue
    else:
        print(m-i,end=" ")


