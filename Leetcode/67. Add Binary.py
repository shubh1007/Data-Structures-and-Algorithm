class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        res = ""
        if len(a) != len(b):
            if len(a) < len(b):
                a,b = b,a
            for i in range(len(a) - len(b)):
                b = "0" + b
            
        for i in range(len(a)-1, -1, -1):
            temp = int(a[i]) + int(b[i]) + carry
            carry = temp // 2
            temp = temp % 2
            res = str(temp) + res
        if carry == 1:
            res = "1" + res
        return res
        
