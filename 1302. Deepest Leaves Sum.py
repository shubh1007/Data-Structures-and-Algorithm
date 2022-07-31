class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution():
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root, None]
        bfs = []        
        level = []
        while len(queue) != 1:
            temp = queue.pop(0)
            if not temp: 
                bfs.append(level)
                level = []
                queue.append(None)
            else: 
                level.append(temp.val)
                if temp.left: 
                    queue.append(temp.left)                
                if temp.right: 
                    queue.append(temp.right)
        return  sum(level)
                    
                
sol = Solution()

root = TreeNode(6)
root.left = TreeNode(7)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(1)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(9)
root.left.right.left = TreeNode(1)
root.left.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)

SUM = sol.deepestLeavesSum(root)
print(SUM)







