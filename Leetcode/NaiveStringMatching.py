class Solution:
    def naviveStringMatching(self, pattern, text):
        M = len(pattern)
        N = len(text)
        for i in range( N - M + 1):
            j = 0
            while (j < M):
                if text[ i + j] != pattern[j]: 
                    break
                j += 1
            if j == M:
                print(f"Pattern found at index: {i}")

# Hello
obj1 = Solution()
txt = "AABAACAADAABAAABAA"
pattern = "AABA"
obj1.naviveStringMatching(pattern, txt)