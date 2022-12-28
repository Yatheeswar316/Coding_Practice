l1=[1,2,4,6,10,20]
l2=[1,3,6,7,7,8]
l3=[]
x=len(l1)+len(l2)-2
print(x)
i,j=0,0
while i+j<x:
    if l1[i]>l2[j]:
        l3.append(l2[j])
        j+=1
    else:
        l3.append(l1[i])
        i+=1

print(l3)

            
        
                