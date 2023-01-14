from collections import defaultdict
class Solution:
    def smallestEquivalentString(self, s1, s2, baseStr):
        union_find = {}
        def find(x):
            if x not in union_find:
                union_find[x] = x
            if x != union_find[x]:
                union_find[x] = find(union_find[x])
            return union_find[x]
        
        def union(x, y):
            X = find(x)
            Y = find(y)
            if X > Y:
                union_find[X] = Y
            else:
                union_find[Y] = X
        
        for i in range(len(s1)):
            union(s1[i], s2[i])
        res = []
        for c in baseStr:
            res.append(find(c))
        return ''.join(res)



s1 = "hello"
s2 = "world"
baseStr = "hold"
sol = Solution()
res = sol.smallestEquivalentString(s1, s2, baseStr)
print(res)
