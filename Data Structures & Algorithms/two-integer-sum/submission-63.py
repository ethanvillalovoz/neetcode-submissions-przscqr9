class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Straightfoward way

        # check if the respective other compliment number exists in list

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return []