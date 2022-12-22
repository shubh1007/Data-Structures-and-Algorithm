class Solution:
    def isSymmetric(self, root):
        if not root: return True
        def helper(node1, node2):
            if not node1 and not node2:
                return True
            if (node1 and not node2) or (not node1 and node2):
                return False
            if node1.val == node2.val:
                return helper(node1.left, node2.right) and helper(node1.right, node2.left)
            else:
                return False
        return helper(root.left, root.right)