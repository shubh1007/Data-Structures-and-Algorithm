class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        hashmap = {}
        for idx, val in enumerate(inorder):hashmap[val] = idx
        def helper(ins, ine, pos, poe):
            if ins > ine or pos > poe: return None
            root = TreeNode(postorder[poe])
            idx = hashmap[postorder[poe]]
            no_elem_to_left = idx - ins
            root.left =  helper(ins, ins + no_elem_to_left - 1, pos, pos + no_elem_to_left - 1)
            root.right = helper(ins + no_elem_to_left + 1, ine, pos + no_elem_to_left, poe - 1)
            return root
        return helper(0, len(inorder) - 1, 0, len(postorder) - 1)

def inorderTraversal(root):
    if not root:
        return
    inorderTraversal(root.left)
    print(root.val, end=" ")
    inorderTraversal(root.right)


def postorderTraversal(root):
    if not root:
        return
    postorderTraversal(root.left)
    postorderTraversal(root.right)
    print(root.val, end=" ")


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
sol = Solution()
root = sol.buildTree(inorder, postorder)


"""
ins = 0,    ine = 4
pos = 0,    poe = 4

numRoot = 1


root = TN(3)




"""


inorderTraversal(root)
print()
postorderTraversal(root)
