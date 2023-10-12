class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        total = sum(nums)

        if total < target:
            return 0

        left = 0
        total = 0
        ans = 999999

        for right in range(len(nums)):

            if nums[left] >= target or nums[right] >= target:
                return 1

            total += nums[right]

            while total >= target:
                ans = min(ans, right - left + 1)
                total -= nums[left]
                left += 1

        return ans
