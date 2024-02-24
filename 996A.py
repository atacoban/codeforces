a=int(input())
count=0
ali=0
 
if a>=100:
    count+=a//100
    a=a%100
    
if a>=20:
    count+=a//20
    a=a%20
   
if a>=10:
    count+=a//10
    a=a%10
   
if a>=5:
    count+=a//5
    a=a%5   
                                                                                     
if a>=1:
    count+=a//1
    a=a%1
 
print(count)