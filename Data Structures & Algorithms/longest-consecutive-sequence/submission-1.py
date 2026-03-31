class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)

        longest = 0
        cur_long = 0

        for num in numSet:

            if num - 1 not in numSet:
                while num + cur_long in numSet:
                    cur_long += 1

                longest = max(longest, cur_long)

                cur_long = 0

        return longest