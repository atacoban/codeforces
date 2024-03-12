c={}
k=1
for i in range(int(input())):
    a=input()
    if a in c:
       c[a]+=k
    else:
        c[a]=1
max_key = max(c, key=lambda x: c[x])
print(max_key)

