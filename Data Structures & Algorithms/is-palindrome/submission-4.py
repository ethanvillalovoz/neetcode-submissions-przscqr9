class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l = 0
        r = len(s) - 1

        while l < r:

            while l < r and not self.is_Alphanumeric(s[l]):
                l += 1

            while l < r and not self.is_Alphanumeric(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l, r = l + 1, r - 1

        return True

    def is_Alphanumeric(self, char: str) -> bool:

        return (ord("A") <= ord(char) <= ord("Z")) \
            or (ord("a") <= ord(char) <= ord("z")) \
            or (ord("0") <= ord(char) <= ord("9"))