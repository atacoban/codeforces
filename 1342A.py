d=[]
for i in range(int(input())):
    x,y=(map(int,input().split()))
    a,b=(map(int,input().split()))
    #print(x,y,a,b)
    adolar=0
    bdolar=0
    if 2*a>=b:
        tmp=min(x,y)
        bdolar=b*tmp
        x=x-tmp
        y=y-tmp                    
        adolar=a*max(x,y)
    else:
        adolar=(x+y)*a

    d.append(adolar+bdolar)
for i in d:
    print(i)







