"""
Runtime: Beats 74.45%
Memory: Beats 43.54%
Binary Search With Extra Checking
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if not nums:
            return 0

        left, right = 0, len(nums) - 1
        if target < nums[left]:
            return left
        elif target > nums[right]:
            return right + 1

        while left <= right:

            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                if nums[mid - 1] < target:
                    return mid
                right = mid - 1
            else:
                if nums[mid + 1] > target:
                    return mid + 1
                left = mid + 1
