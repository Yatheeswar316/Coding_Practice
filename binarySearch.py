from tracemalloc import stop


a=[0,1,2,3,5]
def findMissing():
    for i in range(0,len(a)):
        if i!=a[i]:
            print(i)
            return i

def findMiss():
    if(a[0]!=0):
        print(0)
        return 0
    i=0
    j=len(a)-1
    while(1):
        m=int(i+j/2)
        if(a[m]==m and a[m+1]!=m+1):
            print(m+1)
            return m+1
       
        elif(a[m]!=m):
            j=m

        elif(a[m]==m):
            i=m
       
        

findMiss()
findMissing()


