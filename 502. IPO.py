from heapq import heappop, heappush
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: list[int], capital: list[int]) -> int:
        n = len(capital)
        projects = list(zip(capital, profits))
        projects.sort()
        q = []
        ptr = 0
        for i in range(k):
            while ptr < n and projects[ptr][0] <= w:
                heappush(q, - projects[ptr][1])
                ptr += 1
            if not q:
                break
            w += - heappop(q)
        return w