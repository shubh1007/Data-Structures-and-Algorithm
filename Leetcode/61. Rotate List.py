class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        if not head: return None
        count = 0
        temp = head
        while temp:
            temp = temp.next
            count += 1
        k = k % count
        for i in range(k):
            prev = None
            curr = head
            while curr.next:
                prev = curr
                curr = curr.next
            prev.next = None
            curr.next = head
            head = curr
        return head

def printSLL(root):
    temp = root
    while temp:
        print(temp.val, end = " -> ")
        temp = temp.next
    print()

def createSLL(nums):
    head = None
    temp = None
    for i in nums:
        if head is None: 
            temp = head = Node(i)
        else:
            temp.next = Node(i)
            temp = temp.next
    return head

sol = Solution()
nums = [1, 2, 3, 4, 5]
k = 2
root = createSLL(nums)
printSLL(root)
root = sol.rotateRight(root, k)
printSLL(root)






