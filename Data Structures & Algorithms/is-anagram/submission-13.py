class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # base case - they dont have the same length

        if len(s) != len(t):

            return False

        s_c = defaultdict()
        t_c = defaultdict()


        for i in range(len(t)):

            s_c[s[i]] = 1 + s_c.get(s[i], 0)
            t_c[t[i]] = 1 + t_c.get(t[i], 0)

        return s_c == t_c