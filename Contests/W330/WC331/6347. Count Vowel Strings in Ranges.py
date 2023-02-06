class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        n = len(words)
        vowels = ['a', 'e', 'i', 'o', 'u']
        prefix = [0 for i in range(n + 1)]
        count = 0
        for i in range(n):
            if words[i][0] in vowels and words[i][-1] in vowels:
                count += 1
                prefix[i + 1] = count
            else:
                prefix[i+1] = count
                
        print(prefix)
        output = []
        for start, end in queries:
            temp = abs(prefix[end + 1] - prefix[start])
            output.append(temp)
        return output

words = ["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]
sol = Solution()
res = sol.vowelStrings(words, queries)
print(res)