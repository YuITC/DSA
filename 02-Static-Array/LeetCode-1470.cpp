// 1470. Shuffle the Array
class Solution {
public:
    vector<int> shuffle(vector<int>& nums, int n) {
        for (int i = n; i < nums.size(); i ++)
            nums[i] = nums[i] * 1024 + nums[i-n];

        int idx = 0;
        for (int i = n; i < nums.size(); i ++)
        {
            nums[idx ++] = nums[i] % 1024;
            nums[idx ++] = nums[i] / 1024;
        }
        return nums;
    }
};
