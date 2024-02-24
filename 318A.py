import math
a=list(map(int,input().split()))
if a[0]%2==0:
    if a[0]/2>=a[1]:
        print(a[1]*2-1)
    else:
        print(2*math.ceil(a[1]-(a[0]/2)))
else:
    if math.ceil(a[0]/2)>=a[1]:
        print(a[1]*2-1)
    else:
        print(2*(a[1]-math.ceil(a[0]/2)))

"""
b=[]
c=[]
for i in range(a[0]+1):
    if i%2==1:
        b.append(i)
    else:       
        c.append(i)
c.remove(0)
d=b+c
print(d[a[1]-1])
"""


