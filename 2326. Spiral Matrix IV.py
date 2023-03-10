# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        output = [[-1 for i in range(n)] for j in range(m)]
        temp = head
        left, right = 0, n - 1
        up, down = 0, m - 1
        while left <= right and up <= down and temp:
            for i in range(left, right + 1):
                if temp:
                    output[up][i] = temp.val
                    temp = temp.next
            for i in range(up + 1, down + 1):
                if temp:
                    output[i][right] = temp.val
                    temp = temp.next
            if left < right and up < down:
                for i in range(right - 1, left, -1):
                    if temp:
                        output[down][i] = temp.val
                        temp = temp.next
                for i in range(down, up, -1):
                    if temp:
                        output[i][left] = temp.val
                        temp = temp.next
            left += 1
            right -= 1
            up += 1
            down -= 1
        return output
