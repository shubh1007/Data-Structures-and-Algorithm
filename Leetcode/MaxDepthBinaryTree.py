from LevelOrderTraversal import TreeNode

class Solution:
    def maxDepth(self, root):
        if root == None:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

sol = Solution()
result = sol.maxDepth(root)
print(result)
            

    
