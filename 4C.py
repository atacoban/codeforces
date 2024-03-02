list=[]
a=[]
for i in range(int(input())):
    list.append(input())

dict = {}
 
for i in list:
    if i in dict:
        continue
    else:
        dict[i] = 0

for i in list:
    if dict[i]==0:
        a.append("OK")
        dict[i]+=1
    else:
        a.append(i+str(dict[i]))
        dict[i]+=1

for i in a:
    print(i)