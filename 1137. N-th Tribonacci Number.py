class Solution:
    def tribonacci(self, n: int) -> int:

        if n < 3:
            return 0 if n == 0 else 1

        current = 0
        prev3 = 0
        prev2 = 1
        prev1 = 1

        for i in range(3, n + 1):
            current = prev3 + prev2 + prev1
            prev3 = prev2
            prev2 = prev1
            prev1 = current

        return current
