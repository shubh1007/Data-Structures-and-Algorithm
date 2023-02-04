from collections import Counter, defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Brute Force Approach: 
        #   Check the presence of any of permutation of shorter string in longer string.
        #   Find the permutations of shorter string.
        #   Check whether the permutation is present in longer string or not.
        
        # Using Sorting:
        #   Sort both the substring.
        #   Get the substrings of longer string.
        #   Check whether the substring is smaller string or not.
        
        # Using Hashmap:
        #   Store the frequency of s1 in a dictionary.
        #   Then create a window of size of length of s1.
        #   return True, if the frequency of s1 is same as that of window.
        #   After looping through n2 - n1 return False
        s1Map = Counter(s1)
        n1, n2 = len(s1), len(s2)
        if n1 > n2: return False
        for i in range(n2 - n1 + 1):
            tempMap = defaultdict(int)
            for j in range(n1):
                tempMap[s2[i + j]] = tempMap[s2[i + j]] + 1
            if tempMap.items() == s1Map.items():
                return True
        return False
    
s1 = "ab"
s2 = "eidboaoo"
sol = Solution()
res = sol.checkInclusion(s1, s2)
print(res)
            


             
















