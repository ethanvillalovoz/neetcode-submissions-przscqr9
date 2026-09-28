class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) == 0:
            return True
        
        p = 0

        for i in range(len(t)):
            if p < len(s) and s[p] == t[i]:
                p += 1


        return True if p == len(s) else False
