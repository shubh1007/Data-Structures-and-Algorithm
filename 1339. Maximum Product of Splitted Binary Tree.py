class Solution:
    def maxProduct(self, root):
        self.ans = 0
        def totalSum(root):
            if not root: return 0
            else: return totalSum(root.left) + totalSum(root.right) + root.val
        def productMax(root, total_sum):
            if not root: return 0 
            else:
                subtree = 0
                subtree += productMax(root.left, total_sum) + productMax(root.right, total_sum) + root.val
                self.ans = max(self.ans, subtree * (total_sum - subtree))
            return subtree
        total_sum = totalSum(root)
        productMax(root, total_sum)
        return self.ans % 1000000007
    

