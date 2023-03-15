class TreeNode:
    def __init__(self, val = 0, left = None, right = None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = [root]
        
        while queue:
            node = queue.pop(0)
            
            if node:
                queue.append(node.left)
                queue.append(node.right)
            else:
                break
        
        return not any(queue)
        