class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        ans = 1
        dp = [1] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
                    ans = max(ans, dp[i])

        return ans
