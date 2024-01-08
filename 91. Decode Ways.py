class Solution:
    def numDecodings(self, s: str) -> int:

        if s and s[0] == "0":
            return 0

        dp = {len(s): 1}

        def dfs(index: int):
            if index in dp:
                return dp[index]

            if s and s[index] == "0":
                return 0

            result = dfs(index + 1)
            if ((index + 1 < len(s)) and
                    (s[index] == "1" or (s[index] == "2" and s[index + 1] in "0123456"))):
                result += dfs(index + 2)
            dp[index] = result

            return result

        return dfs(0)
