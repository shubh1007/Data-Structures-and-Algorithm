class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        for i, x in enumerate(nums):
            nums[i] = -x
        heapify(nums)
        c, b, a = -heappop(nums), -heappop(nums), -heappop(nums)
        while True:
            if a + b > c:
                return a + b + c
            try:
                c, b, a = b, a, -heappop(nums)
            except:
                return 0