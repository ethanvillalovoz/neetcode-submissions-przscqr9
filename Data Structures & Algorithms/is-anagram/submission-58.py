class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        counter = {}

        for i in range(len(s)):
            counter[s[i]] = 1 + counter.get(s[i], 0)

        for i in range(len(t)):
            if t[i] in counter and counter[t[i]] - 1 >= 0:
                counter[t[i]] -= 1
            else:
                return False

        return True