class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(next = head)
        stack = []
        
        
