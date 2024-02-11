class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:

        nums.sort()
        cache = {}

        def dfs(i: int):
            if i == len(nums):
                return []

            if i in cache:
                return cache[i]

            result = [nums[i]]
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    temp = [nums[i]] + dfs(j)
                    if len(temp) > len(result):
                        result = temp

            cache[i] = result
            return result

        ans = []
        for i in range(len(nums)):
            temp = dfs(i)
            if (len(temp) > len(ans)):
                ans = temp

        return ans
