s="abcdaefgas"
char=set()
res=0
l=0
for r in range(len(s)):
    while s[r]  in char:
        char.remove(s[l])
        l+=1
    char.add(s[r])
    res=max(res,r-l)
print(res)