class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
        Algorithm:
            1.  Count the number of 0's in the string as n
            2.  Set result to be n initially
            3.  Now traverse through the characters in the string
            4.        if char is '0':
            5.          You don't have to swap this so set n -= 1
            6.          result = min(result, n)
            7.        else:
            8.            char is '1' means you have to swap 
            9.            so n += 1
            10.    return result
        
        Complexity Analysis:
            Time - O(N) # Looping
            Space - O(1) # result variable, and m
    
        Args:   
            s (str): Binary String

        Returns:
            int: Minimum number of flips required to make the string monotonically increasing.
        """

        m = 0
        for i in s:
            if i == '0': 
                m += 1
        ans = m
        for i in s:
            if i == '0':
                m -= 1
                ans = min(ans, m)
            else:
                m += 1
        return ans
    
s = "010110"
sol = Solution()
res = sol.minFlipsMonoIncr(s)
print(res)

