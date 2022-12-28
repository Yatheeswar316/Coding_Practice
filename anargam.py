
def anargam(s1,s2):
    d1={}
    d2={}
    for i in s1:
        d1[i]=1+d1.get(i,0)
    for i in s2:
        d2[i]=1+d2.get(i,0)
    if (d1==d2):
        print("true")
    else:
        print("False")
print(anargam("saaho","osaahyy"))