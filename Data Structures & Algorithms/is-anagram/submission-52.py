class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        count = {}

        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)

        for i in range(len(t)):
            if t[i] not in count or count[t[i]] - 1 < 0:
                return False
            
            count[t[i]] -= 1

        return True