"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root: return None
        stack = [root]
        result = []
        while stack:
            temp = stack.pop(-1)
            result.append(temp.val)
            for i in range(len(temp.children) -1, -1, -1):
                stack.append(temp.children[i])
        return result
            
        