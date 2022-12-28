def rodCut(price,n):
    T=[0]*(n+1)

    for i in range(1,n+1): #i be  the length of rod
        for j in range(1,i+1): #divide rod of length i into j and i-j
            T[i]=max(T[i],price[j-1]+T[i-j])
    print(T)

rodCut([3,5,8,9,10,17],6)