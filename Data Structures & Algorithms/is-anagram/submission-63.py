class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(t) != len(s):
            return False

        count = dict()

        for i in range(len(s)):
            count[s[i]] = 1 + count.get(s[i], 0)

        for i in range(len(t)):
            if t[i] in count and count[t[i]] - 1 >= 0:
                count[t[i]] -= 1
            else:
                return False

        return True