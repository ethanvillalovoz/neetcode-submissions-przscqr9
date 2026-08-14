class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True

        # return False

        # Time: O(n^2)
        # Space: O(1)

        # seen = []

        # for i in range(len(nums)):
        #     if nums[i] in seen:
        #         return True

        #     seen.append(nums[i])

        # return False

        # Time: O(n^2)
        # Space: O(n)

        seen = set()

        for num in nums:
            if num in seen:
                return True

            seen.add(num)

        return False

        # Time: O(n)
        # Space: O(n)