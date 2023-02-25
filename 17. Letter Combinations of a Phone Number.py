class Solution:
    def letterCombinations(self, digits):
        n = list(digits)
        numMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz", 
        }
        output = []
        def backtrack():
            pass


sol = Solution()
digits = "23"
res = sol.letterCombinations(digits)
print(res)