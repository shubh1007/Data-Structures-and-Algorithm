class Solution:
    def findAndReplacePattern(self, words, pattern):
        def isIsomorphic(w, p):
            wmap = {}
            pmap = {}
            for i in range(len(w)):
                a = w[i]
                b = p[i]
                if (a in wmap and wmap[a] != b) or (b in pmap and pmap[b] != b): return False
                wmap[a] = b
                pmap[b] = a
            return False
        
        result = []
        for i in words:
            if isIsomorphic(i, p): result.append(i)
        return result
                
            
                
            