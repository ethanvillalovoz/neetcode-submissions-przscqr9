class Solution:
    def scoreOfString(self, s: str) -> int:
        
        score = 0
        l, r = 0, 1

        while r < len(s):
            score += abs(ord(s[l])-ord(s[r]))
            l, r = l+1, r+1

        return score