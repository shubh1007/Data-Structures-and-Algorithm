class Solution:
    def allPairs(self, A, B, N, M, X):
        A = set(A.sort())
        B = set(B.sort())
        res = []
        for i in list(A):
            if X - i in B:
                res.append([i, X - i])
        final = []
        return res

sol = Solution()
inp1 = "-113 147 65 37 6 -27 -73 109 31 -8 -102 -74 -183 -186 131 40 150 -123 -111 -91 176 170 -4 -165 -49 93 -68 142 171 98 -60 -196 99 69 138 -20 -143 -63 129 -158 -103 -30 73 32 151 136 82 -150 -31 -37 -164 101 -69 -62 -100 -14 111 -97 119 -137 68 -130 -127 -161 124"
inp2 = "-122 102 -67 152 -169 48 -52 -134 33 -91 188 6 -148 -109 -35 64 32 75 198 22 65 -168 185 -66 -127 -147 145 -29 104 51 93 71 129 39 76 10 70"
A = list(map(int, inp1.split()))
B = list(map(int, inp2.split()))
N = 65
M = 37
X = 2
res = sol.allPairs(A, B, N, M, X)
print(res) 
