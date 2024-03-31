a,b=map(int, input().split())
candle=a
count=a
while candle>=b:
    count+= candle // b
    candle=(candle//b) + (candle%b)
print(count)
