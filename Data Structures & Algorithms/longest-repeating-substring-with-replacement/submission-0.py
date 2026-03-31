class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = defaultdict(int)
        l, r = 0, 0
        freqChar = 0
        longest = 0

        while r < len(s):
            count[s[r]] += 1
            freqChar = max(freqChar, count[s[r]])

            while (r-l+1) - freqChar > k:
                count[s[l]] -= 1
                l += 1

            longest = max(longest, (r-l+1))
            r += 1

        return longest