class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
    

class Solution:
    def buildTree(self, preorder, inorder):
        if not inorder or not preorder: return None
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1: idx + 1], inorder[:idx])
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1: ])
        return root

    def inOrder(self, root):
        if not root: return
        self.inOrder(root.left)
        print(f"{root.val}", end = " ")
        self.inOrder(root.right)

    def preOrder(self, root):
        if not root: return
        print(f"{root.val}", end = " ")
        self.preOrder(root.left)
        self.preOrder(root.right)

sol = Solution()
inorder = [9, 3, 15, 20, 7]
preorder = [3, 9, 20, 15, 7]
root = sol.buildTree(preorder, inorder)
print("In Order Traversal: ", end = "\t")
sol.inOrder(root)
print("\nPre Order Traversal: ", end = "\t")
sol.preOrder(root)
