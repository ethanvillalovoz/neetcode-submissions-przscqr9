class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        longest = 0
        cur_longest = 0
        numSet = set(nums)

        for num in numSet:
            if (num-1) not in numSet:            
                while (num + cur_longest) in numSet:
                    cur_longest += 1

                longest = max(longest, cur_longest)
                cur_longest = 0

        return longest     