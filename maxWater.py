from turtle import right


n=[1,8,6,2,5,4,8,3,7]
maxi=0
for i in range(0,len(n)):
    for j in range(1,len(n)):
        newMax=(j-i)*min(n[i],n[j])
        maxi=max(newMax,maxi)
print(maxi)
l=0
r=len(n)-1
m=0
while(l!=r):
    newMax=(r-l)*min(n[l],n[r])
    m=max(m,newMax)
    if(n[l]<n[r]):
        l=l+1
    else:
        r=r-1
print(m)
