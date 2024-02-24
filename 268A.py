a=input()
c=[]
d=[]
x=0

def how_man_seen(lst,tmp):
    count=0
    for j in range(len(lst)):
        if lst[j]==tmp:
            count+=1
    return count

for i in range(int(a)):
    a,b=map(int,input().split())
    c.append(a)
    d.append(b)
for i in c:
    x+=how_man_seen(d,i)


print(x)



    

            

        









