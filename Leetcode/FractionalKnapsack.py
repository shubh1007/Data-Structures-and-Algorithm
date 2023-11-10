class Solution:
    def fractionalKnapsack(n, w, values, weights):
        # code here
        ratio = []
        for i in range(n):
            ratio.append((values[i]/weights[i], values[i], weights[i]))
        ratio.sort(reverse=True)
        ans = 0
        for i in range(n):
            if w == 0:
                break
            if ratio[i][2] <= w:
                ans += ratio[i][1]
                w -= ratio[i][2]
            else:
                ans += ratio[i][0]*w
                w = 0
        return ans
    
        