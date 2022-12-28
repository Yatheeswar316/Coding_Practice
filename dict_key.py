V=[3,2,3,3]
H=[5,5]
flag=True
i,j=0,0
buff=0

while(flag):
    if(buff>=V[j]):
        buff=buff-V[j]
        print("buffer is",buff)
        print("killing",j)
        j+=1
    if(H[i]<V[j]):
        i+=1
    if(H[i]>=V[j] or buff>=V[j]):
        buff=H[i]-V[j]
        print("buffer is",buff)
        print("killing",j)
        j+=1
    if(j==len(V) or i==len(H)):
        flag=False



        
        
        
        
        
        







