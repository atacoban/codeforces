a,b=input().split()
c=map(int,input().split())
c=list(c)
count=0
for i in c:
    if int(b)>=i:
        count+=1
    else:
        count+=2
print(count)












