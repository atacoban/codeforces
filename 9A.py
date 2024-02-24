a = list(map(int, input().split()))
a.sort()
b = ((6-a[1])+1)
if b == 0:
    print("0/1")
if b == 1:
    print("1/6")
if b == 2:
    print("1/3")
if b == 3:
    print("1/2")
if b == 4:
    print("2/3")
if b == 5:
    print("5/6")
if b == 6:
    print("1/1")
