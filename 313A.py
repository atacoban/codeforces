b=list(map(str,*(input().split())))
if b[0]=="-" and b[2]=="0" and len(b)==3:
    print(0)

else:

    if b[0]=="-":
        d=["-"]
        a=[]
        b.remove("-")
        for i in b:
            a.append(int(i))
        if a[-1]>a[-2]:
            a.pop(-1)
        else:
            a.pop(-2)
        for i in a:
            d.append(int(i))
        for i in d:
            print(i,end="")
    else:
        for i in b:
            print(i,end="")

