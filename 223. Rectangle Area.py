class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        A = ax1
        B = ay1
        C = ax2
        D = ay2
        E = bx1
        F = by1
        G = bx2
        H = by2
        return (C-A)*(D-B) + (G-E)*(H-F) - max(0,min(G,C)-max(A,E))*max(0,min(D,H)-max(B,F))
<<<<<<< HEAD

sol = Solution()
res = [-3, 0, 3, 4, 0, -1, 9, 2]
print(sol.computeArea(*res))
=======
>>>>>>> 0054b6a7878fe0f5d064104af0559b659008e036
