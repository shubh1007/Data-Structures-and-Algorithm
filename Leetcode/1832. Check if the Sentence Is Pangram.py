class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        memo = {}
        for i in sentence:
            if i not in memo:
                memo[i] = 1
        return len(memo.values()) == 26
