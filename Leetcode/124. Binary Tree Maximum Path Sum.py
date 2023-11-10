from sys import maxsize

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root):
        self.res = root.val
        def getMaxSubtreePathSum(root):
            if not root: return 0
            leftMax = max(getMaxSubtreePathSum(root.left), 0)
            rightMax = max(getMaxSubtreePathSum(root.right), 0)
            self.res = max(self.res, root.val + leftMax + rightMax)
            return root.val + max(leftMax, rightMax)
        getMaxSubtreePathSum(root)
        return self.res


root = TreeNode(5)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

obj = Solution()
res = obj.maxPathSum(root)
print(f"\nMax Path Sum = {res}")











