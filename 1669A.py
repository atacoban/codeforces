c=[]
for i in range(int(input())):
    a=int(input())
    if 1900 <= a:
        c.append("Division 1")
    elif 1600 <= a <=1899:
        c.append("Division 2")
    elif 1400 <= a <=1599:
        c.append("Division 3")
    else:
        c.append("Division 4")
for i in c:
    print(i)




