c=[]
for i in range(int(input())):
    lenght=input()
    nums=list(map(int,input().split()))
    a=max(nums)
    b=min(nums)
    c.append(a-b)
for i in c:
    print(i)
