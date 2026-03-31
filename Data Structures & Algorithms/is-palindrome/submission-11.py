class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l, r = 0, len(s)-1

        while l < r:
            while l < r and not self.is_alpha(s[l]):
                l += 1
            while l < r and not self.is_alpha(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l, r = l+1, r-1

        return True

    def is_alpha(self, char: str) -> bool:

        return (
            (ord("a") <= ord(char) <= ord("z")) or \
            (ord("0") <= ord(char) <= ord("9")) or \
            (ord("A") <= ord(char) <= ord("Z"))
        )