# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root: return 0
        if root.val < low:
            return self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            return self.rangeSumBST(root.left, low, high)
        leftSum = self.rangeSumBST(root.left, low, high)
        rightSum = self.rangeSumBST(root.right, low, high)
        if root.val >= low and root.val <= high:
            return leftSum + rightSum + root.val
        return leftSum + rightSum
