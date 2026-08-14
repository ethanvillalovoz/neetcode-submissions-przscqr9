class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # if len(s) != len(t):
        #     return False
        
        # count_s = {}
        # count_t = {}

        # for i in range(len(s)):
        #     count_s[s[i]] = 1 + count_s.get(s[i], 0)
        #     count_t[t[i]] = 1 + count_t.get(t[i], 0)

        # return count_s == count_t

        # Time: O(n)
        # Space: O(1)

        if len(s) != len(t):
            return False

        count_s = {}
        count_t = {}

        for char_s, char_t in zip(s, t):
            count_s[char_s] = 1 + count_s.get(char_s, 0)
            count_t[char_t] = 1 + count_t.get(char_t, 0)

        return count_s == count_t
