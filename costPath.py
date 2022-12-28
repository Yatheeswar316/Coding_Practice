cost= [1,100,1,1,1,100,1,1,100,1]
dp0=cost[0]
dp1=cost[1]
for i in range(2,len(cost)):
    curr=cost[i]+min(dp0,dp1)
    dp0=dp1
    dp1=curr
print(min(dp0,dp1))