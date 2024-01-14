class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # whether s[i:len(s)] is valid in wordDict
        # last must be True
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if i + len(w) <= len(s) and s[i:i + len(w)] in wordDict:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break

        return dp[0]
