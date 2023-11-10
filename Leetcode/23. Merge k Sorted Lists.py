class ListNode:
    def __init__(self, x = 0):
        self.val = x
        self.next = None
class Solution:
    def mergeKLists(self, lists):
        nums = []
        for head in lists:
            while head:
                nums.append(head)
                temp = head
                head = head.next
                temp.next = None
        nums.sort(key = lambda x: x.val)
        head = ListNode()
        temp = head
        for node in nums:
            temp.next = node
            temp = temp.next
        return head.next
        