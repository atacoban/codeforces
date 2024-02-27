a=[]
for i in range(int(input())):
    hour,minute=list(map(int,input().split()))
    time=(hour*60)+minute
    countdown=(24*60)-time
    a.append(countdown)
for i in a:
    print(i)
