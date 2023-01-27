class Solution:
    def findConcatenateWordsInADict(self, words: list[str]) -> list[str]:
        def helper(word, dit):
            for i in range(mini, len(word)):
                left = word[: i]
                right = word[i: ]
                if left in dit:
                    if right in dit or helper(right, dit):
                        return True
            return False
            
        res = []
        dit = set(list(words))
        mini = 10000
        for w in words:
            mini = min(mini, len(w))
        for w in words:
            if helper(w, dit):
                res.append(w)
        return res
