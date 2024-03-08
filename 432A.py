a,b=map(int,input().split())
c=[]
count=0
t=list(map(int,input().split()))
for i in t:
    c.append(i)
for index,value in enumerate(c):
    if value+b<=5:
        count+=1
print(count//3)

