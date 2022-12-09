import heapq

class Solution:
    def maxPerformance(self, n, speed, efficiency, k):
        eng = []
        for eff, spd in zip(efficiency, speed):
            eng.append([eff, spd])
        eng.sort(reverse = True)
        
        res, speed = 0, 0
        minHeap = []
        for eff, spd in eng:
            if len(minHeap) == k:
                speed -= heapq.heappop(minHeap)
            speed  += spd
            heapq.heappush(minHeap, spd)
            res = max(res, eff * speed)
        return res % (10 ** 9 + 7)

sol = Solution()
n = 6
speed = [2,10,3,1,5,8]
efficiency = [5,4,3,9,7,2]
k = 2
print(sol.maxPerformance(n, speed, efficiency, k))
