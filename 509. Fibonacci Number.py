class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n

        prev2, prev1 = 0, 1
        for i in range(2, n):
            prev1, prev2 = prev1 + prev2, prev1

        return prev2 + prev1
