from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.leaves = []
        def helper(node, ds):
            ds.append(node.val)
            if not node.left and not node.right:
                self.leaves.append(ds.copy())

                return
            if node.left:
                helper(node.left, ds)
            
            if node.right:
                helper(node.right, ds)
            
            
        res = 0
        helper(root, [])
        print(self.leaves)
        for leaf in self.leaves:
            num = ""
            for node in leaf:
                num += str(node)
            res += int(num)
        return res

