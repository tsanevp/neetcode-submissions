class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        if not prices:
            return res
        
        left = 0
        for right, val in enumerate(prices):
            profit = val - prices[left]
            res = max(res, profit)

            if profit < 0:
                left = right
        
        return res