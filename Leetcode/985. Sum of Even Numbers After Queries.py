class Solution(object):
    def sumEvenAfterQueries(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0 for i in range(n)]
        SUM = 0
        for i in range(n):
            if nums[i] % 2 == 0:  
                SUM += nums[i]
            
        for idx in range(n):
            temp = nums[queries[idx][1]]
            nums[queries[idx][1]] += queries[idx][0]
            if (temp % 2 ==0) and (nums[queries[idx][1]] % 2) == 0:
                SUM += nums[queries[idx][1]] - temp
            elif (temp %2 == 1) and ((nums[queries[idx][1]] % 2) == 0):
                SUM += nums[queries[idx][1]]
            elif (nums[queries[idx][1]] % 2) == 1 and temp % 2 == 0:
                SUM -= temp
            result[idx] = SUM
        return result
                
