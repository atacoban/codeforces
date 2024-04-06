#8 4 2 6
a=int(input())
b=a%4
if a==0:
    print("1")
else:
    if b==1:
        print("8")
    elif b==2:
        print("4")
    elif b==3:
        print("2")
    else:
        print("6")

