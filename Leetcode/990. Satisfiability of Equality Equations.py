class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        uf = {}
        def helper(x):
            if x not in uf: uf[x] = x
            s = []
            while uf[x] != x:
                s.append(x)
                x = uf[x]
            for y in s:uf[y] = x
            return x
        for eq in equations:
            if "==" not in eq: continue
            a, b = helper(eq[0]), helper(eq[-1])
            uf[a] = b
        for eq in equations:
            if "!=" not in eq: continue
            a, b = helper(eq[0]), helper(eq[-1])
            if a == b: return False
        return True
                    
