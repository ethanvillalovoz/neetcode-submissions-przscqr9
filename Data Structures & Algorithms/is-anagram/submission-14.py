class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # base case - they dont have the same length

        if len(s) != len(t):

            return False

        s_c = defaultdict(int)
        t_c = defaultdict(int)


        for i in range(len(t)):

            s_c[s[i]] += 1
            t_c[t[i]] += 1

        return s_c == t_c