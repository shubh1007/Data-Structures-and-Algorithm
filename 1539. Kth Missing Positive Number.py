class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        # For Binary Search to work, the array must be sorted
        # We have taken two pointers, left and right
        # left is the starting index of the array
        # right is the last index of the array
        left, right = 0, len(arr)
        while left <= right:
            # We have taken mid as the middle index of the array
            mid = (left + right) // 2
            # If the difference between the value at mid and mid is less than k
            # example: arr = [1,2,3,4] and k = 2
            # mid = 1 and arr[mid] = 2
            # arr[mid] - mid - 1     < k
            #     2    -  1  - 1 = 0 < 2
            if arr[mid] - mid - 1 < k:
                # We move the left pointer to the right of mid
                left = mid + 1
            else:
                # We move the right pointer to the left of mid
                right = mid - 1
        return left + k
sol = Solution()
arr = [1,2,3,4]
k = 2
res = sol.findKthPositive(arr, k)
print(res)