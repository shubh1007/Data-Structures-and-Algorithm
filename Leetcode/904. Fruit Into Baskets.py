class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        n = len(fruits)
        start, end = 0, 0
        maxLen = 0
        DICT = {}
        while end < n:
            DICT[fruits[end]] = end
            if len(DICT) >= 3:
                minVal = min(DICT.values())
                del DICT[fruits[minVal]]
                start = minVal + 1
            maxLen = max(maxLen, end - start + 1)
            end += 1
        return maxLen


        """
        int n = fruits.size();
        int start = 0, end = 0, maxLen = 0;
        unordered_map<int, int> DICT;
        while (end < n){
            DICT[fruits[end]] = end;
            if (DICT.size() >= 3){
                minVal = min(DICT)
                DICT.erase(fruits[minVal]);
                start = minVal + 1;
            }
            maxLen = max(maxLen, end - start + 1);
            end++;
        }
        return maxLen;

        """





sol = Solution()
fruits = [3,3,3,1,2,1,1,2,3,3,4]
res = sol.totalFruit(fruits)
print(res)
