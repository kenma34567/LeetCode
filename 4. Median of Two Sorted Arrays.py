"""
Runtime: Beats 75.25%
Memory: Beats 53.85%
"""


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        merged = nums1 + nums2
        merged.sort()
        if len(merged) % 2 != 0:
            mid = len(merged) // 2
            median = float(merged[mid])
        else:
            median = (merged[len(merged) // 2 - 1] + merged[len(merged) // 2]) / 2

        print(median)

        return median

