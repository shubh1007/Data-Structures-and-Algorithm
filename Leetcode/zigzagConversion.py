class Solution:
    def convert(self, s, numRows):
        if numRows == 1: return s
        result = ""
        n = len(s)
        increment = 2 * (numRows - 1)
        for row in range(numRows):
            for col in range(row, n, increment):
                result += s[col]
                if row > 0 and row < numRows - 1 and 0 < col + increment - 2 * row < n:
                    result += s[col + increment - 2* row]
        return result
            





        
sol = Solution()
s = "PAYPALISHIRING"
numRows = 3
result = sol.convert(s, numRows)
print(result)
            
        
