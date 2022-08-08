# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return None
        queue = [root, None]
        result = []
        row = []
        while len(queue) != 1:
            temp = queue.pop(0)
            if not temp:
                queue.append(None)
                result.append(row)
                row = []
            else:
                row.append(temp.val)
                if temp.left: 
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
        if row:
            result.append(row)
        return result
                
            
        
        