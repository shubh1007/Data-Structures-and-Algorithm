# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def helper(root, seq):
            if not root:
                return
            if not root.left and not root.right:
                seq.append(root.val)
            helper(root.left, seq)
            helper(root.right, seq)
            return seq
        left = helper(root1, [])
        right = helper(root2, [])
        return left == right
