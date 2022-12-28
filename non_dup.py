a=input()
print(a)
l=list(a)
print(l)
for i in l:
    if l.count(i)==1:
        print(l.index(i)+1)
        break