class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, postorder, inorder):
        if not postorder or not inorder: return None
        root = TreeNode(postorder[len(postorder) - 1])
        idx = inorder.index(postorder[len(postorder) - 1])
        root.left = self.buildTree(postorder[:idx], inorder[:idx])
        root.right = self.buildTree(postorder[idx:len(postorder)-2], inorder[idx+1:])
        return root

    def inOrder(self, root):
        if not root: return
        self.inOrder(root.left)
        print(f"{root.val}", end = " ")
        self.inOrder(root.right)

    def postOrder(self, root):
        if not root: return
        self.inOrder(root.left)
        self.inOrder(root.right)
        print(f"{root.val}", end = " ")
        
sol = Solution()
postorder = [4, 5, 2, 6, 7, 3, 1]
inorder = [4, 2, 5, 1, 6, 3, 7]
root = sol.buildTree(postorder, inorder)
print("In Order: ")
sol.inOrder(root)
print("\nPost Order: ")
sol.postOrder(root)


