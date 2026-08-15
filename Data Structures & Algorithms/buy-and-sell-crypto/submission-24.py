class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0

        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > profit:
                    profit = prices[j] - prices[i]

        return profit

        # Time: O(n^2)
        # Space: O(1)

        profit = 0
        i, j = 0, 0

        while i < len(prices):
            if prices[j] - prices[i] > profit:
                profit = prices[j] - prices[i]
                j += 1

            i += 1

        return prices