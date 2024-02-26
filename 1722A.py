a=[]
for i in range(int(input())):
    lenght=int(input())
    string=input()
    if lenght!=5:
        a.append("NO")
    else:
        if "T" in string and "i" in string and "m" in string and "u" in string and "r" in string:
            a.append("YES")
        else:
            a.append("NO")
for i in a:
    print(i) 