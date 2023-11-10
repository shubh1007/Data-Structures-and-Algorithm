class Solution:
    def findMinArrowShots(self, points):
        points.sort(key = lambda x: x[1])
        tempEnd = points[0][1]
        res = 1
        for start, end in points:
            if start > tempEnd:
                res += 1
                tempEnd = end
        return res


sol = Solution()
points = [[10, 16], [2, 8], [1, 6], [7, 12]]
res = sol.findMinArrowShots(points)
print(res)