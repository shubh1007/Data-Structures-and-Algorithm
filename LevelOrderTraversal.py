class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root):
        if root == None:
            return None
        elif root.left == root.right == None:
            return [root.val]
        
        queue = [root, None]
        temp = root
        result = []
        level = []
        while queue:
            temp = queue.pop(0)
            if temp == None:
                queue.append(None)
                result.append(level)
                level = []
            
            else:
                level.append(temp.val)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            if len(queue) == 1:
                result.append(level)
                return result
        
        
if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print(sol.levelOrder(root))

