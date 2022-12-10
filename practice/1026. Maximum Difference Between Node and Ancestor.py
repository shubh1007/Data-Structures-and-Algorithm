class Node:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root):
        self.v = 0
        def helper(root, imax, imin):
            if not root: return 0
            imax = max(imax, root.val)
            imin = min(imin, root.val)
            self.v = max(self.v, abs(imax - imin))
            helper(root.left, imax, imin)
            helper(root.right, imax, imin)
            return self.v

# nums = list(map(int, input().split()))
# n = len(nums)
# root = None
# root = Node(nums[0])
# temp = root
# for idx, val in enumerate(nums[1:]):
#     left = 2 * idx + 1
#     right = 2 * idx + 2
#     if left < n:




















