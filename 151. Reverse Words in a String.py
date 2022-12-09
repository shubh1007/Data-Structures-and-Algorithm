class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        s = ""
        return " ".join(words[x] for x in range(len(words)-1, -1 , -1))
        
