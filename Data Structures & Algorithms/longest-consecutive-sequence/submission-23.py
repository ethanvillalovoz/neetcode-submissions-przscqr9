class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        length = 0
        numSet = set(nums)

        for num in nums:
            if (num - 1) not in numSet:
                while (num + length) in numSet:
                    length += 1

                longest = max(length, longest)
                length = 0

        return longest