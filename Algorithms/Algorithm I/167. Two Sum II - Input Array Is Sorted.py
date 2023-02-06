class Solution:
    def twoSum(self, numbers: list[int], target: list[int]) -> list[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            currSum = numbers[left] + numbers[right]
            if currSum == target:
                return [left + 1, right + 1]
            elif currSum > target:
                right -= 1
            else:
                left += 1

numbers = [-1, 0]
target = -1
sol = Solution()
res = sol.twoSum(numbers, target)
print(res)

            
