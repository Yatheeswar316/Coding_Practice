nums=["abc","akmi","blaa","ahsja","ahshja","saaho","alla"]
query=['1-4','2-4',"1-3"]
res=[]
vow=("a","e","i","o","u")

for i in nums:
    if(i[0] in vow and i[-1] in vow):
        res.append(1)
    else:
        res.append(0)
count=[]



