input()
a=list(map(int,input().split()))
a.sort(reverse=True)
toplam=0
twin=0
count=0
for i in a:
    toplam+=i
for j in a:
    if toplam//2<twin:
        break
    else:
        count+=1
        twin+=j
        

print(count)









