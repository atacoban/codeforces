b = []
for i in range(int(input())):
    string = input()
    a = int(len(string))
    firsthalf = string[0:a//2]
    lasthalf = string[a//2::]
    if len(string) % 2 == 1:
        b.append("NO")
    else:
        if firsthalf == lasthalf:
            b.append("YES")
        else:
            b.append("NO")
for i in b:
    print(i)
