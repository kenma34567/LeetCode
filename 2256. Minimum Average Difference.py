"""
Runtime: 1120 ms Beats 82.19%
Memory: 26 MB Beats 20.69%
"""

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:

        """
            Construct a prefix sum array
            Calculate according to the formula
        """

        def toPrefixSum(nums: List[int]) -> List[int]:
            prefixSumNums = []
            for i in range(len(nums)):
                if i == 0:
                    prefixSumNums.append(nums[i])
                    continue
                prefixSumNums.append(prefixSumNums[i - 1] + nums[i])
            return prefixSumNums

        prefixSumNums = toPrefixSum(nums)
        print(nums)

        minAvgDif = -1
        minAvgDifIndex = -1
        for i in range(len(prefixSumNums)):
            left = prefixSumNums[i] // (i + 1)
            right = prefixSumNums[-1] - prefixSumNums[i]
            if right != 0:
                right //= (len(nums) - i - 1)
            avgDif = abs(left - right)
            print("avgDif", avgDif)
            if avgDif == 0:
                return i

            if avgDif < minAvgDif or minAvgDif < 0:
                minAvgDif = avgDif
                minAvgDifIndex = i

        return minAvgDifIndex

