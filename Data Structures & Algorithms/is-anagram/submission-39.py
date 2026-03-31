class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_c = Counter(s)
        t_c = Counter(t)

        return t_c == s_c