class Solution:
    def intToRoman(self, num):
        symVal = [
            ["I",  1],
            ["IV", 4],
            ["V",  5],
            ["IX", 9],
            ["X",  10],
            ["XL", 40],
            ["L",  50],
            ["XC", 90],
            ["C",  100],
            ["CD", 400],
            ["D",  500],
            ["CM",  900],
            ["M",  1000]
            ]

        i = len(symVal) - 1
        result = ""
        while num:
            quo = num//symVal[i][1]
            if quo > 0:
                result += (symVal[i][0]* quo)
            num = num % symVal[i][1]
            i -= 1
        return result


sol = Solution()
num = 100
for num in range(1, 1000):
    result = sol.intToRoman(num)
    print(f"{num}: {result}")
