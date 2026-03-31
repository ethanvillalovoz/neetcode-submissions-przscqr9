class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        history = defaultdict(int)

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff not in history:
                history[nums[i]] = i
            else:
                return [history[diff], i]

        return []