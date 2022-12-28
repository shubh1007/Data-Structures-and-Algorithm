import heapq

# change polarity of elements in piles
# create a heap
# Now maximum element is the root of heap
# loop through elements k times
#   set curr to heap's root element 
#   push -(-curr +int(curr/2)) into heap
# return sum of elements in heap


class Solution:
    def minStoneSum(self, piles, k):
        piles = [-i for i in piles]
        heapq.heapify(piles)
        for i in range(k):
            curr = heapq.heappop(piles)
            heapq.heappush(piles, -(-curr + int(curr/2)))
        return -sum(piles)
        
piles = [5, 4, 9]
k = 2
sol = Solution()
res = sol.minStoneSum(piles, k)
print(res)