"""
Runtime: Beats 77.21%
Memory: Beats 57.26%
"""


class Solution:

    def maxArea(self, height: List[int]) -> int:

        if not height: return 0

        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:

            left_height = height[left]
            right_height = height[right]

            max_area = max(max_area, (right - left) * min(left_height, right_height))

            if left_height < right_height:
                left += 1
            else:
                right -= 1

        return max_area
