a=list(map(int,(input().split())))
b=list(map(int, str(a[0])))
lucky=[4,7,44,47,74,77,444,447,474,477,744,747,777]
c=[]
d=[]
for i in b:
    if i!=4 and i!=7:
        for i in lucky:
            if a[0]%i==0:
                d.append(True)
                break
            else:
                continue
                
        
    else:
        c.append("True")

if len(c)==len(b) or len(d)>=1:
    print("YES")
else:
    print("NO")




