class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # My solution - HashMap Counter
        # counter = {}

        # for i in nums:

        #     if i not in counter:
        #         counter[i] = 1
        #     else:
        #         counter[i] += 1

        #     if counter[i] > 1:
        #         return True

        # return False


        # Brute Force Solution
        for i in range(0, len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    print(nums[i])
                    print(nums[j])
                    return True

        return False
