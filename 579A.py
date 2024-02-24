Neededbacteria=int(input())
a=Neededbacteria
x=True
count=1
while x==True:
    if a==1:
        break
    if a%2==0:
        a=a//2
    else:
        a=a-1
        count+=1
    
print(count)






