V=[3,2,3,2]
H=[5,5]
flag=True
i,j=0,0
buff=H[0]

while(1):
    buff = buff - V[j]
    if buff < 0:
        print("hero defeated i=", i)
        i+=1
        if i<len(H):
            buff = H[i]
    elif buff == 0: 
        print("hero defeated but also got exhauseted i,j=",i,j)
        i+=1
        j+=1
        if i<len(H):
            buff = H[i]
    else:
        print("hero defeated villain i,j=", i,j)
        j+=1
    if j>=len(V):
        print("villains all defeated")
        break
    if i>=len(H):
        print("heroes all defeated go home")
        break
    
        


        
        
        
        
        
        







