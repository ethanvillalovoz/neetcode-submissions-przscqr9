class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)

        longest = 0

        cur_length = 0

        for num in numSet:

            if (num - 1) not in numSet:
                while (num + cur_length) in numSet:
                    cur_length += 1

                longest = max(longest, cur_length)
                cur_length = 0
            
            else:
                continue

        return longest