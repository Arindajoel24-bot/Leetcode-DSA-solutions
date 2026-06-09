class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = float('inf')
        for n, v in enumerate(prices):
            lowest = min(v, lowest)
            profit = max(v - lowest, profit)

        return profit