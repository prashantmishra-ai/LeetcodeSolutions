class Solution {
public:
        void permuteRecursive(vector<int> nums, int begin, vector<vector<int>>& result) {
        if (begin >= nums.size()) {
            result.push_back(nums);
            return;
        }

        for (int i = begin; i < nums.size(); i++) {
            swap(nums[begin], nums[i]);
            permuteRecursive(nums, begin + 1, result);
            // no need to swap back because we make a new copy of nums at the next recursion level
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
                vector<vector<int>> result;
        permuteRecursive(nums, 0, result);
        return result;
    }
};