from requests import head


class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseBeteen(self, head, left, right):
        prev = None
        curr = head
        left, right = left - 1, right - 2
        #left = 1     prev = None     curr = 1
        while left and curr:  
            prev = curr
            curr = curr.next
            left -= 1
        #left = 0     prev = 1     curr = 2
        prevHead = prev
        currHead = curr
        #right = 3     prev = None     curr = 2
        prev = None
        while right and curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            right -= 1
        if prevHead: prevHead.next = prev
        if currHead: currHead.next = curr
        return head
    def insert(self, val):
        temp = None
        head = None
        for i in val:
            if not temp: head = temp = ListNode(i)
            else: 
                temp.next = ListNode(i)
                temp = temp.next
        return head
        
sol = Solution()
head = sol.insert([1,2,3,4,5])
l, r = 1, 5

result = sol.reverseBeteen(head, l, r)
while result:
    print(result.val, end = " ")
    result = result.next
print()