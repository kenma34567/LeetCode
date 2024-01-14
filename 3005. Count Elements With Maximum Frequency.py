class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        counterNums = Counter(nums)
        maxFreq = max(counterNums.values())
        ans = 0
        for k, v in counterNums.items():
            if v == maxFreq:
                ans += v

        return ans
