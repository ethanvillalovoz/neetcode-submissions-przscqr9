class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        longest = 0
        l, r = 0, 0
        charSet = set()

        while r < len(s):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            longest = max(longest, len(charSet))
            r += 1
        
        return longest