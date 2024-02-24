
mi=0
ch=0
for i in range(int(input())):
    a=list(map(int,input().split()))   
    if a[0]>a[1]:
        mi+=1
    elif a[0]<a[1]:
        ch+=1
    else:
        continue
if mi<ch:
    print("Chris")
elif mi>ch:
    print("Mishka")
else:
    print("Friendship is magic!^^")









