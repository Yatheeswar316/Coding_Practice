def DemandFarm(a,b,c,d,e):
    a=a%3
    b=b%3
    c=c%3
    temp=[a,b,c]
    temp.sort()
    if temp==[0,0,2]:
        x=min(d+e,2*e)
        y=e
        print(x,y)
    elif temp==[0,0,1]:
        x=min(d,2*e)
        y=2*e
        print(x,y)
    elif temp==[0,1,2]:
        x=e
        y=3*e
        print(x,y)
    elif temp==[0,1,1]:
        x=min(d,e)
        y=min(4*e,2*d+e)
        print(x,y)
    elif temp==[0,2,2]:
        x=min(e,d+2*e)
        y=min(2*e,d+2*e)
        print(x,y)
    else:
        x=min(d,3*e)
        y=0
        print(x,y)
print(DemandFarm(397,26,38,361,778))
