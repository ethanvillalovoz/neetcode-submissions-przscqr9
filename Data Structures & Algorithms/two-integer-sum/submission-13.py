class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        history = defaultdict(int)

        for i in range(len(nums)):
            res = target - nums[i]

            if res in history:
                return [history[res], i]
            else:
                history[nums[i]] = i

        return []