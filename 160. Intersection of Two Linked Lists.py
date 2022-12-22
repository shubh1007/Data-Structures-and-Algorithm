class ListNode:
    def __init__(self, val = 0, next = None):        
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA, headB):
        t1, t2 = headA, headB
        while t1 != t2:
            t1 = t1.next if t1 else headB
            t2 = t2.next if t2 else headA
        return t1.val


t1 = ListNode(1)
t1.next = ListNode(2)

t1.next.next = ListNode(100)
t1.next.next.next = ListNode(200)
t1.next.next.next.next = ListNode(300)

t2 = ListNode(10)
t2.next = ListNode(20)
t2.next.next = ListNode(30)

t2.next.next.next = t1.next.next
t2.next.next.next.next = t1.next.next.next
t2.next.next.next.next.next = t1.next.next.next.next

sol = Solution()
res = sol.getIntersectionNode(t1, t2)
print(res)









