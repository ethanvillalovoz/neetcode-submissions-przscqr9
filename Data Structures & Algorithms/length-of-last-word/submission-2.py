class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        res = []
        word = ""
        print(word)

        for i in range(len(s) + 1):
            if i < len(s) and s[i] != " ":
                word += s[i]
            else:
                if word != "":
                    res.append(word)
                    word = ""
                    
        print(res)
        return len(res[-1])