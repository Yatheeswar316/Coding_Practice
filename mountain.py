
def fun(l):
    prev=l[0]
    maxi=0
    for i in range(1,len(l)):
        maxi=max(maxi,l[i]-prev+1)
        prev=min(l[i],l[i]-prev+1)
        

fun([-1,1,1,1])



