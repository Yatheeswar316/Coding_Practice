        dic={}
        for i in nums:
            if i not in dic:
                dic[i]=0
            dic[i]+=1
        maxi=0
        ans=0
        for x in dic:
            print(x)
            if(dic[x]>maxi):
                maxi=dic[x]
                ans=x
        return ans
            