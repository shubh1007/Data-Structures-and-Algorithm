class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        def SORT(mat, row, col, m, n):
            value = []
            r, c = row, col
            while r<m and c<n:
                value.append(mat[r][c])
                r += 1
                c += 1
            value.sort()
            
            r, c = row, col
            ind = 0
            while r<m and c<n:
                mat[r][c] = value[ind]
                r += 1
                c += 1
                ind += 1
                
        m = len(mat)
        n = len(mat[0])
        for col in range(n):
            SORT(mat, 0, col, m, n)
        for row in range(1, m):
            SORT(mat, row, 0, m, n)
        return mat
        