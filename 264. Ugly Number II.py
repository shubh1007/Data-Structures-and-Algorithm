class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        nums = [1]
        i2 = i3 = i5 = 0
        while len(nums) < n:
            num2 = nums[i2] * 2
            num3 = nums[i3] * 3
            num5 = nums[i5] * 5
            num = min(num2, num3, num5)
            nums.append(num)
            if num == num2:
                i2 += 1
            if num == num3:
                i3 += 1
            if num == num5:
                i5 += 1
        return nums[-1]