class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lb, ub = 0, len(nums)-1
        while lb<=ub:
            mid = (lb+ub)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                ub = mid-1
            else:
                lb = mid+1
        return -1
