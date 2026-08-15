class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Straightfoward way

        # check if the respective other compliment number exists in list

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # return []

        # Time: O(n^2)
        # Space: O(1)

        # Optimized

        prev = defaultdict()

        for i, num in enumerate(nums):
            diff = target - num

            if diff in prev:
                return [prev[diff], i]

            prev[num] = i

        return []

        # Time: O(n)
        # Space: O(n)