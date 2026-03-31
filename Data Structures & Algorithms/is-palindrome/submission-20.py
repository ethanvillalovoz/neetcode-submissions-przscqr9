class Solution:
    def isPalindrome(self, s: str) -> bool:

        palindrome = ""

        for c in s:
            if self.is_alpha(c):
                palindrome += c.lower()

        return palindrome == palindrome[::-1]

    def is_alpha(self, c: str = "a") -> bool:

        return (
            (ord("A") <= ord(c) <= ord("Z")) or \
            (ord("a") <= ord(c) <= ord("z")) or \
            (ord("0") <= ord(c) <= ord("9"))
        )