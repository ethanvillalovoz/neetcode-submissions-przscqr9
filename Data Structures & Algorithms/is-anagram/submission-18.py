class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        t_c = defaultdict(int)
        s_c = defaultdict(int)

        for i in range(len(s)):
            t_c[t[i]] += 1
            s_c[s[i]] += 1

        return t_c == s_c