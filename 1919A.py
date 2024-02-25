WinnerList=[]
for i in range (int(input())):
    alice,bob = map(int,(input().split()))
    if (alice + bob)%2==0:
        WinnerList.append("Bob")
    else:
        WinnerList.append("Alice")

for i in WinnerList:
    print(i)



