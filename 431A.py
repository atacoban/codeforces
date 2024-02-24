a=list(map(int,input().split())) 
b=list(map(int,*(input().split()))) 
count=0
for i in b:
    if i==1:
        count+=a[0]
    elif i==2:
        count+=a[1]
    elif i==3:
        count+=a[2]
    else:
        count+=a[3]

print(count)








