class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        prefix=[nums[0]]
        for i in range(1,len(nums)):
            prefix.append(prefix[-1]+nums[i])
        mini=float("inf")
        idx=-1
        n=len(nums)
        for i in range(n-1):
            ans=abs((prefix[i]//(i+1)-(prefix[n-1]-prefix[i])//(n-i-1)))
            if(ans<mini):
                idx=i
                mini=ans
        if(prefix[-1]//n<mini):
            return n-1
        return idx

