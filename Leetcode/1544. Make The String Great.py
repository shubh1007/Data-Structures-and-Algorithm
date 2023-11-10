class Solution:
    def makeGood(self, s: str) -> str:
        r = []
        for c in s:
            if r and abs (ord (r[-1])-ord(c))==32: r.pop(-1)
            else:
                r.append(c)
        return ''.join(r)
        
    
            
