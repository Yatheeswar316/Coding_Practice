def trappingWater(arr):
        l,r=0,len(arr)-1
        leftMax,rightMax=arr[l],arr[r]
        res=0
        while l<r:
            if leftMax>rightMax:
                r-=1
                rightMax=max(rightMax,arr[r])
                res+=rightMax-arr[r]
                
            else:
                l+=1
                leftMax=max(leftMax,arr[l])
                res+=leftMax-arr[l]
        return res