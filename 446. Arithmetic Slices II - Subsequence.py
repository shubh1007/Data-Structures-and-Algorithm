class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        size = len(nums)
        ans = 0
        dp = [collections.defaultdict(int) for x in range(size)]
        for x in range(size):
            for y in range(x):
                delta = nums[x] - nums[y]
                dp[x][delta] += 1
                if delta in dp[y]:
                    dp[x][delta] += dp[y][delta]
                    ans += dp[y][delta]
        return ans
