
def noOfGlasses(x):
    res=[[1]]
    flag=True
    sum=1

    while(x>sum):
        temp=[]
        for i in range(len(res[-1])+1):
            temp.append(1)
        y=len(temp)
        print(y)
        sum=sum+y
        res.append(temp)
    print(res)

noOfGlasses(13)


    
    
