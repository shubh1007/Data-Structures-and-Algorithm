# Kadane's Algorithm
# 1. set currSum = 0
# 2. set maxSum = -inf
# 3. loop: i = 0 to n - 1
    # set currSum += arr[i]
    # if currSum > maxSum:
        # set maxSum = currSum
    # if currSum < 0:
        # set currSum = 0
# 4. return maxSum


class Solution:
    def kadaneAlgo(self, arr):
        currSum = 0
        maxSum = -float("inf")
        left, right = 0, 0
        for i in range(len(arr)):
            currSum += arr[i]
            if currSum > maxSum: 
                maxSum = currSum
                right = i
            elif currSum < 0: 
                currSum = 0
                left = i
                right = i
            print(f"left = {left} right = {right}")
    
sol = Solution()
sol.kadaneAlgo([-2, 3, -1, 2])
