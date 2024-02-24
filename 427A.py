a=input()
b=map(int,input().split())
b=list(b)
count=0
police=0
for index, value in enumerate(b):
    if index==0:
        if value==-1:
            count+=1
        else:
            police+=value
    else:
        if value>=1:
            police+=value
        else:
            if police==0:
                count+=1
            else:
                police-=1
       
print(count)










