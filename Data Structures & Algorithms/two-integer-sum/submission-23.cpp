class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        unordered_map<int, int> prevMap;
        int diff;

        for (int i = 0; i < nums.size(); i++) {
            diff = target - nums[i];

            if (prevMap.find(diff) != prevMap.end()) {
                return {prevMap[diff], i};
            }
            else {
                prevMap.insert({nums[i], i});
            }
        }

        return {};
    }
};
