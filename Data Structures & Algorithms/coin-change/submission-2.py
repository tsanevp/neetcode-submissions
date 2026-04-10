class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for amount in range(1, amount + 1):
            for coin in coins:
                curr = amount - coin
                if curr >= 0:
                    dp[amount] = min(dp[amount], 1 + dp[curr])
        
        return dp[-1] if dp[-1] < (amount + 1) else -1