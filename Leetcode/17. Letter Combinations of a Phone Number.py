class Solution:
    def letterCombinations(self, digits):
        numMap = {
            0 : "",
            1 : "",
            2 : "abc",
            3 : "def",
            4 : "ghi",
            5 : "jkl",
            6 : "mno",
            7 : "pqrs",
            8 : "tuv",
            9 : "wxyz"
        }
        output = []
        def backtrack(num, string):
            if num == "":
                return
            if num == 0:
                output.append(string)
                return
            num = int(num)
            last_ligit = num % 10
            num = num // 10
            for i in numMap[last_ligit]:
                backtrack(num, i + string)
        backtrack(digits, "")
        return output
    
sol = Solution()
digits = "23"
res = sol.letterCombinations(digits)
print(res)