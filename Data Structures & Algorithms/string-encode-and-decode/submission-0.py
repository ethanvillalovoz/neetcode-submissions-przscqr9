class Solution:

    def encode(self, strs: List[str]) -> str:

        str_encode = ""

        for s in strs:

            str_encode += str(len(s)) + "#" + s

        return str_encode

    def decode(self, s: str) -> List[str]:

        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            size = int(s[i:j])
            i = j + 1
            j = i + size

            res.append(s[i:j])

            i = j

        return res




