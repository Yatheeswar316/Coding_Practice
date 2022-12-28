def count(nums,target):
    res=0
    if target<0:
        return 0
    if target==0:
        return 1
    for i in nums:
        res+=count(nums,target-i)
    return res

def dcount(S, target):
 
    T = [0] * (target + 1)
    T[0] = 1
 
    for i in range(len(S)):
        j = S[i]
        while j <= target:
            T[j] += T[j - S[i]]
            j = j + 1
 
    return T[target]
print(count([1,2,3],4))
print(dcount([1,2,5],5))

