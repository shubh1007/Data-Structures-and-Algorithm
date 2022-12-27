class Solution:
    def maximumBags(self, capacity, rocks, additionalRocks):
        remaining = []
        for i, j in zip(capacity, rocks):
            remaining.append(i - j)
        full = 0
        remaining.sort()
        for i in remaining:
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
