from LevelOrderTraversal import TreeNode

class Solution:
    def diameter(self, root):
        def height(root):
            if root == None: return 0
            return max(height(root.left), height(root.right)) + 1

        
        if root == None: return 0
        leftHeight = height(root.left)
        rightHeight = height(root.right)
        leftDiameter = self.diameter(root.left)
        rightDiameter = self.diameter(root.right)
        return max(leftDiameter, rightDiameter, max(leftHeight, rightHeight) + 1)

    def inOrder(self, root):
        if not root: return None
        self.inOrder(root.left)
        print(root.val, end = " ")
        self.inOrder(root.right)
    


root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.left.left = TreeNode(5)
root.right.left.right = TreeNode(6)
root.right.right = TreeNode(7)
root.right.right.left = TreeNode(8)
root.right.right.right = TreeNode(9)

sol = Solution()
result = sol.diameter(root)
sol.inOrder(root)
print()
print(result)

        
