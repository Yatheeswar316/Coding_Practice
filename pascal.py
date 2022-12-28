def Pascal(a):
    res=[[1]]
    #res=[[1],[1,1],[1,2,1],[1,3,3,1]]

    
    for i in range(a-1):

        temp=[0]+res[-1]+[0]
        #[0,1,0]
        row=[]
        for j in range(len(res[-1])+1):
            row.append(temp[j]+temp[j+1])
            print(row)
        res.append(row)
    print(res)

print(Pascal(5))
        