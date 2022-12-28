l=[2,3]
ans=[0,1]
for i in range(2,10):
    x=ans[i-1]+ans[i-2]
    ans.append(x)

print(ans)


