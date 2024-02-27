ata, n = map(int, input().split())
a = []
b = 0
for i in range(int(n)):
    a.append(list(map(int, input().split())))
a.sort()

for i in a:
    if ata > i[0]:
        ata += i[1]
    else:
        b += 1
        print("NO")
        break
if b == 0:
    print("YES")
