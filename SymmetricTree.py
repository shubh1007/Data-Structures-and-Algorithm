from LevelOrderTraversal import TreeNode

class Solution:
    def isSymmetric(self, root):
        def helper(leftRoot, rightRoot):
            if not leftRoot and not rightRoot: return True
            if leftRoot and rightRoot:
                if leftRoot.val == rightRoot.val:
                    return helper(leftRoot.left, rightRoot.right) and helper(leftRoot.right, rightRoot.left)
            return False
                
        if not root: return True
        if not root.left and not root.right: return True
        return helper(root.left, root.right)
            
            


        

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

sol = Solution()
result = sol.isSymmetric(root)
print(result)
