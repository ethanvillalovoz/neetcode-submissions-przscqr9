class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        cur_sum = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                cur_sum += nums[j]
                max_sum = max(cur_sum, max_sum)

            cur_sum = 0

        return max_sum