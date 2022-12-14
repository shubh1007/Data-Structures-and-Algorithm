class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root, k):
        """Given the root of a binary search tree, and an integer k, 
        return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

        Args:
            root (TreeNode): root of a binary search tree
            k (int): 1-indexed value of k

        Returns:
            int: return kth smallest value (1-indexed) of the BST
        
        Complexity:
            Time: O(H + k) to build a traversal and those traversal are done from stack
            Space: O(H) to keep track of traversal where H is the height of tree
        """
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if not k: return root.val
            root = root.right

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
k = 1

sol = Solution()
result = sol.kthSmallest(root, k)
print(result)



