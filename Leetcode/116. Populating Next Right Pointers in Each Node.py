class Node:
    def __init__(self, val = 0, left = None, right = None, next = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
         
class Solution:
    def connect(self, root):
        if not root: return None
        queue = [root, None]
        while len(queue) != 1:
            temp = queue.pop(0)
            if not temp:
                queue.append(None)
                continue
            temp.next = queue[0]
            if temp.left: queue.append(temp.left)
            if temp.right: queue.append(temp.right)
        return root

root = Node(1)
root.left = Node(2) 
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

sol = Solution()
root = sol.connect(root)
print(root.next)
print(root.left.next.val)
print(root.right.next)
print(root.left.left.next.val)
print(root.left.right.next.val)
print(root.right.left.next.val)
print(root.right.right.next)











