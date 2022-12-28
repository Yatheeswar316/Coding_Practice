def SubArraySum(nums,target):
    l,r=0,0
    curSum=0
    while(r>=l and l<len(nums) and r<len(nums)):
        if curSum>target:
            curSum-=nums[l]
            l+=1
        elif curSum<target:
            curSum+=nums[r]
            r+=1
        if curSum==target:
            print(l,r)
            break
SubArraySum([1,3,5,6,2],10)