class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        if not nums:
            return []

        prevMap = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[num] = i

        return []