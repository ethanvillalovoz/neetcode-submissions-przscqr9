class Solution:
    def scoreOfString(self, s: str) -> int:
        
        score = 0

        for i in range(len(s)-1):
            if i + 1 in range(len(s)):
                score += abs(ord(s[i])-ord(s[i+1]))
            else:
                score += ord(s[i])

        return score