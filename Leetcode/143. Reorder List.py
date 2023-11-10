class Solution:
    def reorderList(self, head) -> None:
        first = []
        second = []
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        mid = (count // 2) + (0 if count % 2 == 0 else 1)
        current = head
        index = 0
        while current:
            if index < mid:
                first.append(current)
            else:
                second.append(current)
            current = current.next
            index += 1
        second = list(reversed(second))
        current = first.pop(0)
        for i in range(count - 1):
            if i % 2 == 0:
                current.next = second.pop(0)
            else:
                current.next = first.pop(0)
            current = current.next
        current.next = None
















