class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        count = [0] * 26

        for char1, char2 in zip(s, t):
            count[ord(char1) - ord("a")] += 1
            count[ord(char2) - ord("a")] -= 1

        for val in count:
            if val != 0:
                return False

        return True