a=input().split()
c=0
k=240-int(a[1])
count=0
for i in range(int(a[0])):
    c=c+5*(i+1)
    if c <= k:      
        count+=1      
    else:
        break
print(count)
