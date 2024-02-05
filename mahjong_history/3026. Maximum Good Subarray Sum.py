class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = [0] * len(nums)
        prefixSum[0] = nums[0]
        for i in range(1, len(nums)):
            prefixSum[i] = prefixSum[i - 1] + nums[i]
        # print("prefix", prefixSum)

        indexDict = {}
        res = float("-inf")
        for i, n in enumerate(nums):
            target1 = n + k
            target2 = n - k
            if target1 in indexDict:
                index = indexDict[target1]
                currentSum = prefixSum[i] - prefixSum[index - 1] if index > 0 else prefixSum[i]
                res = max(res, currentSum)
            if target2 in indexDict:
                index = indexDict[target2]
                currentSum = prefixSum[i] - prefixSum[index - 1] if index > 0 else prefixSum[i]
                res = max(res, currentSum)
            # print("I", n, res)

            if nums[i] in indexDict:
                index = indexDict[nums[i]]
                rangeSum = prefixSum[i] - prefixSum[index - 1] if index > 0 else prefixSum[i]
                # currentSum = prefixSum[i]-prefixSum[index]
                # print("prefixSum[i]", prefixSum[i], prefixSum[index-1] if index > 0 else prefixSum[index], rangeSum)
                if rangeSum < nums[i]:
                    indexDict[nums[i]] = i

            if nums[i] not in indexDict:
                indexDict[nums[i]] = i

        return res if res != float("-inf") else 0
