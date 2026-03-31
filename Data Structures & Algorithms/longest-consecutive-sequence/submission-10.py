class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        cur_longest = 0
        numSet = set(nums)

        for num in numSet:
            if (num - 1) in numSet:
                continue
            else:
                while num + cur_longest in numSet:
                    cur_longest += 1

                longest = max(cur_longest, longest)
                cur_longest = 0

        return longest