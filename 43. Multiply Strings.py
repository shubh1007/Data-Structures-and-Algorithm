class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        hm = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9
        }
        list1 = list(num1)
        list2 = list(num2)
        num1 = 0
        num2 = 0
        for i in list1:
            num1 = (num1 * 10) + hm[i] 
        for i in list2:
            num2 = (num2 * 10) + hm[i]
        return str(num1 * num2)

sol = Solution()
num1 = "2"
num2 = "3"
res = sol.multiply(num1, num2)
print(res)