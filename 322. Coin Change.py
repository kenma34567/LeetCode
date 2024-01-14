class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [float("inf")] * (amount+1)
        dp[0] = 0
        pointer = 0
        while pointer < amount+1:
            for c in coins:
                if pointer-c < 0:
                    continue
                dp[pointer] = min(dp[pointer], dp[pointer-c]+1)
            pointer += 1

        return dp[amount] if dp[amount] != float("inf") else -1
