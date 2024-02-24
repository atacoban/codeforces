a=input()
c=[]
for i in a:
    if i=="H":
        c.append("yes")
        
    elif i=="Q":
        c.append("yes")
        
    elif i=="+":
        c.append("no")
      
    elif i=="9":
        c.append("yes")
      
    else:
        c.append("no")
if "yes" in c:
    print("YES")
else:
    print("NO")
      

