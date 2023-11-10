class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        myHash = {}
        def traverse(i, j):
            if (i, j) in myHash: return myHash[(i,j)]
            if i >= m or j >= n: return 0
            elif i == m-1 and j == n-1: return 1
            down = traverse(i+1, j)
            right = traverse(i, j + 1)
            myHash[(i, j)] = down + right
            return down + right
        return traverse(0,0)

sol = Solution()
m, n = (3, 7)
print(sol.uniquePaths(m, n))

            
            