import math

class Solution:
    def evelRPN(self, tokens):
        stack = []
        for i in tokens:
            if i in ["+", "-", "*", "/"]:
                b = stack.pop()
                a = stack.pop()
                if i == "+": stack.append(a + b)
                elif i == "-": stack.append(a - b)
                elif i == "*": stack.append(a * b)
                else: stack.append(int(a / b))
            else:
                stack.append(int(i))
        return stack.pop()

sol = Solution()
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
result = sol.evelRPN(tokens)
print(result)