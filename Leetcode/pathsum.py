class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root, targetSum):
        def helper(node, currSum):
            if node == None: return False
            currSum += node.val
            if not node.left and not node.right: return currSum == targetSum
            return helper(node.left, currSum) or helper(node.right, currSum)

        return helper(root, 0)


        
        
        
root = TreeNode(0)

root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)

root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

sol = Solution()
targetSum = 22

result = sol.hasPathSum(root, targetSum)
print(result)

