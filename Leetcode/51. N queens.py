class Solution():
    def nQueens(self, n):
        # initializing the sets
        cols = set()
        positiveDiag = set()
        negativeDiag = set()
        # creating the chess board of n x n
        grid = [["0" for i in range(n)] for i in range(n)]
        result = []
        # this method will be used for backtracking of this DP problem
        def traverse(row):
            if row == n:
                copy = ["".join(r) for r in grid] 
                result.append(copy)
                return
            for col in range(n):
                # if col is invalid we will continue traversing through other col
                if col in cols or (row + col) in positiveDiag or (row - col) in negativeDiag:    
                    continue
                # if the col is valid we will add the queen in the specified row and col
                cols.add(col)
                positiveDiag.add(row + col)
                negativeDiag.add(row - col)
                grid[row][col] = "1"
                # 
                traverse(row + 1)
                
                cols.remove(col)
                positiveDiag.remove(row + col)
                negativeDiag.remove(row - col)
                grid[row][col] = "."
                
        traverse(0)
        return result
    
sol = Solution()
result = sol.nQueens(10)
for i in result:
    for j in i:
        print(j)
    print()