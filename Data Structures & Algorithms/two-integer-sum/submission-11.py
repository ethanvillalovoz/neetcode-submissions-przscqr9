class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        history = defaultdict(int)

        for i in range(len(nums)):
            res = target - nums[i]

            if res not in history:
                history[nums[i]] = i
            else:
                return [history[res], i]

        return False