class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        count = {}

        for i in range(len(s)):
            if s[i] not in count:
                count[s[i]] = 1
            else:
                count[s[i]] += 1

        for i in range(len(t)):
            if t[i] in count:
                count[t[i]] -= 1
            else:
                return False

        for i in range(len(t)):
            if count[t[i]] == 0:
                continue
            else:
                return False

        return True