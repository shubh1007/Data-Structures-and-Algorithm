class Solution:
    def generate(self, numRows):
        res = [[1]]
        for i in range(numRows-1):
            row = [0] + res[-1] + [0]
            nextrow = []
            for j in range(len(row)-1):
                nextrow.append(row[j] + row[j+1])
            res.append(nextrow)
        return res

sol = Solution()
numRows = 100
print(sol.generate(numRows))
        
        