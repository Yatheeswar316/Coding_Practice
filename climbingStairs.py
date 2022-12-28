n=3
one,two=1,1
if(n==1):
    print(1)

for i in range(n-1):
    temp=one
    one=one+two
    two=temp
    print(one)