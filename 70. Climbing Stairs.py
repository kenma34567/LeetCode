class Solution:
    def climbStairs(self, n: int) -> int:
        prev1, prev2 = 1, 1
        current = 1
        for i in range(n - 2, -1, -1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current

        return current
