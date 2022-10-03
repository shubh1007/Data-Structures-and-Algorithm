class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        n=len(s)
        i=0
        res=0
        while(i<n):
            ch=s[i]
            total=0
            maxVal=0
            while(i<n and s[i]==ch):
                maxVal=max(maxVal,cost[i])
                total+=cost[i]
                i+=1
            res+=total-maxVal
        return res

        
