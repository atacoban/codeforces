def Num(x):
    if x==1:
        return False
    if x%2==1:
        return True
    else:
        return Num(x/2)  
b=[]
for i in range(int(input())):
    a=int(input())
    if Num(a):
        b.append("Yes")
    else:
        b.append("No")
for i in b:
    print(i)







