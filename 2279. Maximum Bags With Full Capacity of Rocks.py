class Solution:
    def maximumBags(self, capacity, rocks, additionalRocks):
        for i in range(len(rocks)):
            capacity[i] -= rocks[i]
        full = 0
        capacity.sort()
        for i in capacity:
            if additionalRocks >= i:
                additionalRocks -= i
                full += 1
            else:
                break
        return full

sol = Solution()
capacity = [2, 3, 4, 5]
rocks = [1, 2, 4, 4]
additionalRocks = 2
res = sol.maximumBags(capacity, rocks, additionalRocks)
print(res)
