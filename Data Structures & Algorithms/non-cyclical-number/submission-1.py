class Solution:
    def isHappy(self, n: int) -> bool:
        
        slow, fast = n, self.sumOfSquares(n)

        while slow != fast:
            slow = self.sumOfSquares(slow)
            fast = self.sumOfSquares(fast)
            fast = self.sumOfSquares(fast)

        return True if fast == 1 else False

    def sumOfSquares(self, n: int) -> int:
        
        res = 0

        while n:
            digit = (n % 10)
            digit = digit ** 2
            res += digit
            n //= 10

        return res