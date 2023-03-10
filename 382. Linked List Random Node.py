# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.nums = []
        temp = head
        while temp:
            self.nums.append(temp.val)
            temp = temp.next
    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()