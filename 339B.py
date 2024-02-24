a,b=map(int,input().split())
c=list(map(int,input().split()))
d=0
d+=c[0]-1
for index,value in enumerate(c):
    if index==len(c)-1:
        break
    else:
        if value>c[index+1]:
            d+=(a+c[index+1])-value
        elif value<c[index+1]:
            d+=c[index+1]-value
        else:
            d+=0
print(d)










