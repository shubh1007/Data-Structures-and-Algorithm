from LevelOrderTraversal import TreeNode

def hasPathSum(root, targetSum):
    def helper(node, currSum):
        if not node: return False
        currSum += node.val
        if not node.left and not node.right: return currSum == targetSum
        return helper(node.left, currSum) or helper(node.right, currSum)
    return helper(root, 0)
        


























class Solution:        
    def hasPathSum(self, root, targetSum):
        def helper(root, targetSum):
            if root == None and targetSum != 0:
                return False
            elif root == None:
                return True

            if targetSum == 0:
                return True
            
            left = helper(root.left, targetSum - root.val)
            right = helper(root.right, targetSum - root.val)
            
            return left or right
            
        if root == None:
            return False
        else:
            return helper(root, targetSum)
        
        

root = TreeNode(5)
root.left = TreeNode(4)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right = TreeNode(8)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

obj1 = Solution()

targetSum = 26
result = hasPathSum(root, targetSum)
print(result)
