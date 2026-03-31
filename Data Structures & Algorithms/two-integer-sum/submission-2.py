class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        history = {}

        for i in range(len(nums)):

            result = target - nums[i]

            if result in history:

                return [history[result], i]

            else:
                history[nums[i]] = i
        
        return False