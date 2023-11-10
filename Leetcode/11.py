class Solution:
    @staticmethod
    def maxArea(height):
        """
        BRUTE FORCE
        maxArea = 0
        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                area = (r - l) * min(height[l], height[r])
                maxArea = max(maxArea, area)
        return maxArea
        """
        # LINEAR TIME COMPLEXITY
        maxArea = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            maxArea = max(area, maxArea)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxArea
    


height = [1,8,6,2,5,4,8,3,7]
result = Solution.maxArea(height)
print(result)
        
        
