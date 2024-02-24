Liste1=[]
def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return False
    return True

for i in range(int(input())):
    A,B=(map(int,input().split()))
    k=1
    m1=1
    if isprime(B)==True:
        k=B
        m1=1
        m2=B-1
        x=A*B
        y=k*m1
        z=k*m2
        if y!=z!=x and y+z==x:
            Liste1.append("YES")
            Liste1.append([y,z,x])
            break
    elif isprime(B)==False:
        k=1
        m1=1
        m2=B-1
        x=A*B
        y=k*m1
        z=k*m2
        if y!=z!=x and y+z==x:
            Liste1.append("YES")
            Liste1.append([y,z,x])
            break
    else:
        k=1
        m1=1
        m2=B-1
        x=A*B
        y=k*m1
        z=k*m2
        if y!=z!=x and y+z==x:
            Liste1.append("YES")
            Liste1.append([y,z,x])
            break
    
        
print(Liste1)
