class Solution:
    def maximum69Number (self, num: int) -> int:
        num = list(str(num))
        i  = 0
        while i < len(num):
            if num[i] == '6': 
                num[i] = '9'
                break
            i += 1
        return int("".join(x for x in num))
    
                
            
            
