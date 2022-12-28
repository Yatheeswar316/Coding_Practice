def NumOfWays(N,exp):
    ctr={}
    ctr[0]=1
    ctr[1]=1
    for i in range(2,N+1):
        if i in exp:
            ctr[i]=0
        else:
            ctr[i]=ctr[i-1]+ctr[i-2]
    print(ctr)

NumOfWays(4,[1,3])        
