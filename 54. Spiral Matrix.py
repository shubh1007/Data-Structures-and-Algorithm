from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        left = 0
        right = n - 1
        up = 0
        down = m - 1
        i = 0
        j = 0
        output = []
        while left <= right and up <= down:
            for i in range(left, right + 1):
                output.append(matrix[up][i])
            for i in range(up + 1, down + 1):
                output.append(matrix[i][right])
            if left < right and up < down:
                for i in range(right - 1, left, -1):
                    output.append(matrix[down][i])
                for i in range(down, up, -1):
                    output.append(matrix[i][left])
            left += 1
            right -= 1
            up += 1
            down -= 1
        return output

sol = Solution()
print(sol.spiralOrder([
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ]))