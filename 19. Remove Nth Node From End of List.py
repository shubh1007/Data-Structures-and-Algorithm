# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        temp = head
        while temp:
            temp = temp.next
            count += 1
        N = count - n
        temp = head 
        prev = None
        while N:
            prev = temp
            temp = temp.next
            N -= 1
        if prev and temp:
            prev.next = temp.next
        elif prev is None:
            head = head.next
        else:
            prev.next = None
        return head
