class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        orderMap = {}
        for index, value in enumerate(order):
            orderMap[value] = index
        
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                if words[i][j] != words[i + 1][j]:
                    if orderMap[words[i][j]] > orderMap[words[i + 1][j]]:
                        return False
                    break
        return True