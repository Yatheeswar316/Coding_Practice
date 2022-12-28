def maxProduct(nums):
    res=max(nums)
    currMax,currMin=1,1

    for i in nums:
        if i==0:
            currMax,currMin=1,1
        else:
            temp=currMax*i
            currMax=max(currMin*i,temp,i)
            currMin=min(temp,i,currMin*i)
        res=max(res,currMax)
    return res
print(maxProduct([2,3,-2,4]))