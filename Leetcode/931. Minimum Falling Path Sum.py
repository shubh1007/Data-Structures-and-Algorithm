class Solution:
    def minFallingPathSum(self, matrix)->int:
        """Calculates and returns the minimum falling path sum 
        from first row to the last row of the 2D matrix provided.

        Args:
            matrix (List[List[int]]): 2D matrix of integer type.

        Returns:
            int: returns the minimum path sum value from first row to 
            the last row of the given matrix.
        """
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                left = matrix[i - 1][j - 1] if j - 1 >= 0 else float("inf")
                center = matrix[i - 1][j] 
                right = matrix[i - 1][j + 1] if j + 1 < len(matrix[0]) else float("inf")
                matrix[i][j] += min(left, center, right)
        return min(matrix[-1])

matrix = [[2,1,3],[6,5,4],[7,8,9]]
sol = Solution()
res = sol.minFallingPathSum(matrix)
print(res)