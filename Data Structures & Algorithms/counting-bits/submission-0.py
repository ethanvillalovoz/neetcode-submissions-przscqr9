class Solution:
    def countBits(self, n: int) -> List[int]:
        
        res = []

        for i in range(n+1):
            num = 0
            while i:
                num += 1
                i &= (i-1)
            res.append(num)

        return res