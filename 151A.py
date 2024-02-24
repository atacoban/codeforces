b=map(int,input().split())
b=list(b)

d=(b[1]*b[2])//b[6]
c=(b[3]*b[4])
f=(b[5]//b[7])
g=[d,c,f]
g.sort()
print(g[0]//b[0])






