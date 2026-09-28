class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        if len(t) == 0:
            return 0

        p = 0

        for i in range(len(s)):
            if p < len(t) and t[p] == s[i]:
                p += 1

        return len(t[p:])