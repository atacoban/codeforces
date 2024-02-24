from itertools import permutations
import math
cevap=[]
def myfunc(liste):
    newlist=[]
    for index,num in enumerate(liste):
        temp=math.gcd(num,liste[((index+1)%len(liste))])
        newlist.append(temp)
    return newlist

for i in range(int(input())):
    nums=int(input())
    max=0
    a=[]
    for l in permutations(range(1,nums+1),nums):
        d=myfunc(l)
        m=len(set(d))
        if(max<m):
            max=m
            a=l
    cevap.append(a)

for i in cevap:
    for j in i:
        print(j, " ", end='')
    print()











