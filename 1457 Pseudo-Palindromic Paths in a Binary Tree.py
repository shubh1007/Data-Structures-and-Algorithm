class Solution:
    def pseudoPalindromicPaths (self, root: TreeNode) -> int:
        def dfs(node):
            cur[node.val] = not cur[node.val]
            if not(node.left or node.right):
                if cur.count(False) <= 1:
                    res[0] += 1
                    cur[node.val] = not cur[node.val]
                    return
                
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            cur[node.val] = not cur[node.val]
        
        res = [0]
        cur = [True] * 10
        dfs(root)
        return res[0]
