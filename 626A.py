from itertools import combinations

count=0

a=int(input())

b=input()
 
res = [b[x:y] for x, y in combinations(range(len(b) + 1), r = 2)]

for i in res:

    if i.count('D')==i.count('U') and i.count('L')==i.count('R'):
        
        count+=1

print(count)





