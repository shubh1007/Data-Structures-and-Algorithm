class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root):
        if not root: return None
        Q = [root, None]
        result = []
        flag = 1
        res = []
        while len(Q) != 1:
            temp = Q.pop(0)
            if not temp:
                result.append(res.copy())
                res = []
                flag = 1 - flag 
                Q.reverse()
                Q.append(None)
            else:
                res.append(temp.val)
                if not flag:
                    if temp.right: Q.append(temp.right)
                    if temp.left: Q.append(temp.left)
                else:
                    if temp.left: Q.append(temp.left)
                    if temp.right: Q.append(temp.right)
        if res:
            result.append(res)
        return result

root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.right = TreeNode(3)
root.right.right = TreeNode(5)

sol = Solution()
res = sol.zigzagLevelOrder(root)
print(res)





                

