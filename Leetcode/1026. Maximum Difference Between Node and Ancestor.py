from sys import maxsize
class Node:
    def __init__(self, val = 0, left = None, right = None):
        """ Creating the instance of Node. This is a constructor method.

        Args:
            val (int, optional): The key value of Node. Defaults to 0.
            left (_type_, optional): Points to left child. Defaults to None.
            right (_type_, optional): Points to right child. Defaults to None.
        """
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root):
        self.v = 0
        def helper(root, imax, imin):
            if not root: return 0
            imax = max(imax, root.val)
            imin = min(imin, root.val)
            self.v = max(self.v, abs(imax - imin))
            helper(root.left, imax, imin)
            helper(root.right, imax, imin)
            return self.v
        return helper(root, -maxsize + 1, maxsize)



        # def helper(root, max_ = -maxsize + 1, min_ = maxsize, v = 0):
        #     if not root: return 0
        #     max_ = max(max_, root.val)
        #     min_ = min(min_, root.val)
        #     v = max(v, abs(max_ - min_))
        #     helper(root.left, max_, min_, v)
        #     helper(root.right, max_, min_, v)
        #     return v
        # return helper(root, v = -maxsize + 1)
        
            




head = Node(8)
head.left = Node(3)
head.left.left = Node(1)
head.left.right = Node(6)
head.left.right.left = Node(4)
head.left.right.right = Node(7)
head.right = Node(10)
head.right.right = Node(14)
head.right.right.left = Node(13)

sol = Solution()
result = sol.maxAncestorDiff(head)
print(f"Max Ancestor Difference : {result}")























