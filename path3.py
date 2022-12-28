import sys
a = int(input())
b =[]
for i in range(a):
    b.append(int(input()))
for i in range(a):
    t = b[i]
    for j in range(2):
        t = b[t]
    if t == i:
        print("YES",i)
        sys.exit(0)
print("NO")
[1,2,3,1]
[2,3,3,0]