a = []
b = []
input()
g = list(map(int, input().split()))
for i in g:
    if i % 2 == 0:
        a.append(i)
    else:
        b.append(i)
if len(a) == 1:
    c = a[0]
if len(b) == 1:
    c = b[0]
for index, value in enumerate(g):
    if value == c:
        print(index+1)
