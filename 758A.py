a=int(input())
b=list(map(int,input().split()))
b.sort()
count=0
for i in b:
    count+=b[-1]-i
print(count)



