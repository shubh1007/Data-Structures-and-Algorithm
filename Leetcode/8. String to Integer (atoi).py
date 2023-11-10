class Solution:
    def myAtoi(self, s: str) -> int:
        
        def will_exceed(val, sign, next_val):
            if sign == 1:
                if INT_LIMIT_BY_10 < val:
                    return MAX_INT
                elif INT_LIMIT_BY_10 == val and next_val and next_val > 7:
                    return MAX_INT
                return None
            else:

                if INT_LIMIT_BY_10 < val:
                    return MIN_INT
                elif INT_LIMIT_BY_10 == val and next_val and next_val > 8:
                    return MIN_INT
                return None

        s = s.strip(' ')
        
        if not s:
            return 0
        
        sign = 1
        if s[0] in {'+', '-'}:
            sign = -1 if s[0] == '-' else 1
            s = s[1:]

        MAX_INT = 2**31 -1
        MIN_INT = - 2**31
        INT_LIMIT_BY_10 = 214748364
        
        
        val = 0
        for i, c in enumerate(s):
            if not c.isdigit():
                break
            next_val = ord(c) - ord('0')
            print(next_val)
            limit_val = will_exceed(val, sign, next_val)
            if limit_val:
                return limit_val
            
            val = val * 10 + next_val
        return sign * val