class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        l = length = 0
        substring = set()

        for r in range(len(s)):
            while substring and s[r] in substring:
                substring.remove(s[l])
                l += 1

            substring.add(s[r])
            length = max(length, r-l+1)

        return length