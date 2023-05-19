"""
Merge the strings "word1" and "word2" by alternating the letters from each string, starting with "word1". If one string is longer than the other, append the remaining letters to the end of the merged string. Return the final merged string.
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index1, index2 = 0, 0
        res = ""
        flag = 0
        while index1 < len(word1) and index2 < len(word2):
            if flag == 0:
                res += word1[index1]
                index1 += 1
                flag = 1
            else:
                res += word2[index2]
                index2 += 1
                flag = 0
        while index1 < len(word1):
            res += word1[index1]
            index1 += 1
        while index2 < len(word2):
            res += word2[index2]
            index2 += 1
        return res


