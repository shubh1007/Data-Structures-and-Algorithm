from typing import List
class Solution:
    def maxSatisfaction(self, satisfaction: List[int]):
        satisfaction.sort()
        n = len(satisfaction)
        max_sum = satisfaction[n - 1]
        cum_sum = satisfaction[n - 1]
        val = satisfaction[n - 1]
        for i in range(n - 2, -1, -1):
            cum_sum += satisfaction[i]
            val += cum_sum
            max_sum = max(max_sum, val)
        return max_sum if max_sum > 0 else 0
    
if __name__ == '__main__':
    inputs = [[-1, -8, 0, 5, -9], [-2, 5, -1, 0, 3, -3]]
    for satisfaction in inputs:
        print(Solution().maxSatisfaction(satisfaction))
