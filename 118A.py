a=list(map(str,*(input().lower().split())))
c=[]
for i in a:
    if i == "a" or i == "o" or i == "y" or i == "e" or i == "u" or i == "i":
        continue
    else:
        c.append(".")
        c.append(i)  
for i in c:
    print(i,end="")












