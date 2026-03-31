class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l, r = 0, 0
        longest = 0
        counter = defaultdict(int)
        freqChar = 0

        while r < len(s):
            counter[s[r]] += 1
            freqChar = max(freqChar, counter[s[r]])

            while (r-l+1) - freqChar > k:
                counter[s[l]] -= 1
                l += 1

            longest = max(longest, (r-l+1))
            r += 1

        return longest