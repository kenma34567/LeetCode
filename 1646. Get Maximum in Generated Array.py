class Solution:
    def getMaximumGenerated(self, n: int) -> int:

        if n < 1:
            return 0

        nums = [0] * (n + 1)
        nums[1] = 1
        ans = 1
        for i in range(1, n // 2 + 1):
            nums[2 * i] = nums[i]
            if 2 * i + 1 <= n:
                nums[2 * i + 1] = nums[i] + nums[i + 1]
                ans = max(ans, nums[2 * i + 1])
            ans = max(ans, nums[2 * i])

        return ans
