import itertools
#num,count=map(int,input().split())
num=5
c=3
base=[]
for i in range(num-1):
    base.append((num-i-2) * 'a' + 'b' + i * 'a' + 'b')
group=1
sum=0
for i in range(1,c):
    sum+=i
    if(c>sum):
        group+=1

n=0
for i in range(group):
    n+=i

k=list(base[group])
k[-1] = "a"
k[-group-n]="b"
for i in k:
    print(i,end="")


    