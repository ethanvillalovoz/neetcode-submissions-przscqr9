class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        curMin = curMax = 1

        for num in nums:
            temp = curMax*num
            curMax = max(curMax*num, curMin*num, num)
            curMin = min(temp, curMin*num, num)
            res = max(curMax, res)

        return res