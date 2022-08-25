class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        myHash = {}
        for i in magazine:
            if i not in myHash:
                myHash[i] = 1
            else:
                myHash[i] += 1
        
        for j in ransomNote:
            if j not in myHash:
                return False
            if myHash[j] < 1:
                return False
            else:
                myHash[j] -= 1
            
        return True
                
            
