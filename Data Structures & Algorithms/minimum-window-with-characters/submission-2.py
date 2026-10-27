class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""

        count, window = defaultdict(int), defaultdict(int)

        for c in t:
            count[c] += 1

        have, need = 0, len(count)
        res, length = [-1, -1], float("inf")

        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if window[c] == count[c]:
                have += 1

            while have == need:
                if (r - l + 1) < length:
                    res = [l, r]
                    length = r - l + 1

                window[s[l]] -= 1

                if window[s[l]] < count[s[l]]:
                    have -= 1

                l += 1

        l, r = res

        return s[l:r+1] if length != float("inf") else ""