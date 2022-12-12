from sys import maxsize

class Node:
    def __init__(self, val = 0):
        self.val = val
        self.left = self.right = None
        
class Solution:
    def bstFromPreorder(self, preorder):
        """Create Binary Search Tree from Preorder array

        Args:
            preorder (List[int]): List of preorder traversal sequence.

        Returns:
            TreeNode: Root node of the newly created Binary Search Tree. 
        
        Time Complexity: O(3*N) - Traversing a node three times in the worst complexity namely root, left, right
        Space Complexity: O(1) - No extra stack space is required, just tracking the value.
        """
        self. i = 0
        def helper(preorder, ub):
            if self.i == len(preorder) or preorder[self.i] > ub: return None
            newNode = Node(preorder[self.i])
            self.i += 1
            newNode.left = helper(preorder, newNode.val)
            newNode.right = helper(preorder, ub)
            return newNode
        return helper(preorder, maxsize)

def preOrderTraversal(root):
    if not root: return
    print(root.val, end = ", ")
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)


sol = Solution()
preorder = [8,5,1,7,10,12]
root = sol.bstFromPreorder(preorder)
preOrderTraversal(root)








