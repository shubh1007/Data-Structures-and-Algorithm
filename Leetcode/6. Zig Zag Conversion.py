class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: return s
        result = ""
        n = len(s)
        for row in range(numRows):
            increment = 2*(numRows-1)
            for col in range(row, len(s), increment ):
                result += s[col]
                if row > 0 and row < numRows - 1 and 0 < col + increment - 2*row < n:
                    result += s[col + increment - 2*row]
        return result
