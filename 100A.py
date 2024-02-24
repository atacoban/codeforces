import random
mylist=[]
k=[]
c=0
t=0
while c<10000:
    for i in range(1,101):
        mylist.append(i)
    random.shuffle(mylist)

    count=0
    a=1

    while mylist[a-1]!=1:
        a=mylist[a-1]
        count+=1
    k.append(count)
    c+=1
    mylist=[]
for i in k:
    t+=i
print(k)
print(t/10000)












