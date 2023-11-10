class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        p1, p2 = 0, 0
        
        for word, freq in count.items():
            if word[0] == word[1]:
                p1 = max(p1, freq % 2)
                p2 += freq//2 * 2
            else:
                p2 += min(freq, count[word[::-1]])
                
        return (p1 + p2) * 2
                
