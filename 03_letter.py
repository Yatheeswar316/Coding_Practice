def minTime(nums):
    t=0
    w=0
    l,r=0,0
    while(r<len(nums)):
        t=t+nums[r]
        r+=1
        
