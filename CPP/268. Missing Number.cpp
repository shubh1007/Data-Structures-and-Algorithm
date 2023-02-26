class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size(), SUM = 0;
        for (int i = 0; i<n; i++){
            SUM += nums[i];
        }
        int res = (n*(n+1))/2 - SUM;
        return res;
        
    }
};