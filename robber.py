nums=[1,3,5,6,3,2,5,9]
def robbery(nums):
    rob1,rob2=0,0
    #[rob1,rob2,i,i+1,......]
    for i in nums:
        currMax=max(rob1+i,rob2)
        rob1=rob2
        rob2=currMax
    return rob2
print(robbery(nums)) 