class Solution:

    def encode(self, strs: List[str]) -> str:

        # we can acheive this by creating some delimiter to know 
        # the length of each string

        res = ""

        for s in strs:

            res += str(len(s)) + "#" + s

        return res

    def decode(self, s: str) -> List[str]:

        output = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            size = int(s[i:j])

            i = j + 1
            j += size + 1

            output.append(s[i:j])

            i = j

        return output