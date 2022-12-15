class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        """Construct Binary Tree from inorder and postorder traversal

        Args:
            inorder (List[int]): inorder sequence of Binary Tree
            postorder (List[int]): postorder sequence of Binary Tree

        Returns:
            TreeNode: returns root node of newly created Binary Tree
        """
        hashmap = {}
        for idx, val in enumerate(inorder): hashmap[val] = idx
        def helper(ins, ine, pos, poe):
            if ins > ine or pos > poe: return None
            root = TreeNode(postorder[poe])
            idx = hashmap[postorder[poe]]
            elem = idx - ins
            root.left = helper(ins, ins + elem - 1, pos, pos + elem - 1)
            root.right = helper(ins + elem + 1, ine, pos + elem, poe - 1)
            return root
        return helper(0, len(inorder) - 1, 0, len(postorder) - 1)
    