class Solution:
    def myAtoi(self, s: str) -> int:
        # STEP 1: Ignoring leading whitespaces
        # STEP 2: Identify the sign
        # STEP 3: Identify the number
        # STEP 4: Break if whitespaces found
        # STEP 5: Identfy the range
        MIN_INT = -2**31
        MAX_INT = 2**31 - 1
        sign = 1
        num = 0
        idx = 0
        n = len(s)
        while idx < n and s[idx] == " ":
            idx += 1
        if idx < n and s[idx] == "-":
            sign = -1
            idx += 1
        elif idx < n and s[idx] == "+":
            idx += 1
        
        while idx < n and s[idx].isdigit():
            num = (num * 10) + int(s[idx])
            idx += 1
        if idx == n:
            if num < MIN_INT: return MIN_INT
            if num >= MAX_INT: return MAX_INT
            return num * sign
        else:
            return 0

sol = Solution()
s = "words and 987"
result = sol.myAtoi(s)
print(result)
        
