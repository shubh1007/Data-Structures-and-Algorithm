from collections import defaultdict
class Solution:
    def distinctNames(self, ideas: list[str]) -> int:
        wordMap = defaultdict(set)
        for word in ideas:
            wordMap[word[0]].add(word[1:])
        res = 0
        for C1 in wordMap:
            for C2 in wordMap:
                if C1 == C2: continue
                intersection = 0
                for word in wordMap[C1]:
                    if word in wordMap[C2]:
                        intersection += 1
                D1 = len(wordMap[C1]) - intersection
                D2 = len(wordMap[C2]) - intersection
                res += D1 * D2
        return res

