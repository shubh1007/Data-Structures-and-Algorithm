class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        N = len(A)
        ct = collections.Counter()
        for i, row in enumerate(A):
            for j, col in enumerate(row):
                if col:
                    for i2, row2 in enumerate(B):
                        for j2, col2 in enumerate(row2):
                            if col2:
                                ct[i - i2, j - j2] += 1
        return max(ct.values() or [0])
