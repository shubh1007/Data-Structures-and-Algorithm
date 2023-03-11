from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        def helper(i, j ):
            if i > j: return None
            mid = (i + j) // 2
            root = TreeNode(values[mid])
            root.left = helper(i, mid - 1)
            root.right = helper(mid + 1, j)
            return root
        return helper(0, len(values) - 1)
