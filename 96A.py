a=list(map(int,*(input().split()))) 
c=False
team1=0
team0=0
for i in a:
    if i==1:
        team1+=1
        if team1>=7:
            c=True
            break
        team0=0
    elif i==0:
        team0+=1
        if team0>=7:
            c=True
            break
        team1=0
if c:
    print("YES")
else:
    print("NO") 








