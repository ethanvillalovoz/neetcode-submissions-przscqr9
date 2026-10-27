class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        length = 0
        longest = 0
        charSet = set(nums)

        for num in nums:
            if (num - 1) not in charSet:
                while (num + length) in charSet:
                    length += 1

                longest = max(longest, length)
                length = 0

        return longest