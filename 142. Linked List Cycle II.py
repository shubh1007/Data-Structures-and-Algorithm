# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        visited = set()
        temp = head
        while temp:
            if temp not in visited:
                visited.add(temp)
                temp = temp.next
            else:
                return temp
                