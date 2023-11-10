


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    

class Solution:
    def flatten(self, root):
        def dfs(root):
            if not root: return None
            leftTail = dfs(root.left)
            rightTail = dfs(root.right)
            
            if root.left: 
                leftTail.right = root.right
                root.right = root.left
                root.left = None
                
            return rightTail or leftTail or root
        dfs(root)
                    
sol = Solution()

# 1,2,5,3,4,null,6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.left.left.right = TreeNode(6)

sol.flatten(root)
print(root)
while root: 
    print(root.val, end = " ")
    root = root.right
                    
                                    
                    
                    
                    
                    
                    
                    