a,b,c=map(int,input().split())
if a%c==0:
    d=int(a/c)
else:
    d=int(a/c)+1

if b%c==0:
    f=int(b/c)
else:
    f=int(b/c)+1
print(f*d)
