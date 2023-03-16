from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # stores index of inorder elements 
        # inorder_elements : index
        hm = {}
        for idx, val in enumerate(inorder):
            hm[val] = idx 
        # four pointers:
        # inorder start, inorder end, postorder start, postorder end
        def helper(ins, ine, pos, poe):
            # base case
            if ins > ine or pos > poe:
                return None
            # create a node with postorder_end value
            node = TreeNode(postorder[poe])
            # split the left and right children for node
            idx = hm[postorder[poe]]
            # get the number of elements for left child 
            # we get this from inorder list
            left = idx - ins
            # set the left and right child of node
            # left child: 
            #   inorder: ins, ins - no of elements to left - 1(exclude middle element)
            #   postorder: pos, pos + no of elements to left - 1(0 indexed)
            # right child:
            #   inorder:  ins - no of elements to left + 1, ine
            #   postorder: pos + no of elements to left, poe - 1(exclude last element)

            node.left = helper(ins, ins + left - 1, pos, pos + left - 1)
            node.right = helper(ins + left + 1, ine, pos + left, poe - 1)
            return node
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
