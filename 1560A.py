a=[]
c=[]
for i in range (5000):
    if i%10!=3 and i%3!=0:
        a.append(i)

for i in range(int(input())):
    b=int(input())
    c.append(a[b-1])
for i in c:
    print(i)



