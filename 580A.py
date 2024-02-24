input()
k=[]
a=list(map(int,input().split()))  
count=0
for index, value in enumerate(a):
    if len(a)==1:
        k.append(0)
    if index!=len(a)-1:
        if a[index+1]>=a[index]:
            count+=1
            k.append(count)
        else:
            count=0
if len(k)==0:
    print(1)
else:
    print(max(k)+1)











