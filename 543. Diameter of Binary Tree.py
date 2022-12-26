class Solution:
    def diameterOfBinaryTree(self, root):
        self.res = 0
        def helper(root):
            if not root: return 0
            left = helper(root.left)
            right = helper(root.right)
            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        helper(root)
        return self.res