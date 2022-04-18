"""
Runtime: Beats 91.1%
Memory: Beats 11.8%
Simple Binary Search then find left and right starting from that targetPos
"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def binarySearch(nums: List[int], target: int) -> int:

            if not nums:
                return -1
            elif len(nums) == 1:
                return 0 if nums[0] == target else -1

            left = 0
            right = len(nums) - 1

            while left < right:

                mid = left + (right - left) // 2
                if target == nums[mid]:
                    return mid
                elif target == nums[left]:
                    return left
                elif target == nums[right]:
                    return right

                if left == mid or right == mid:
                    break

                if target < nums[mid]:
                    right = mid
                else:
                    left = mid

            return -1

        targetPos = binarySearch(nums, target)
        print("TA", targetPos)
        if targetPos == -1:
            return [-1, -1]
        else:
            left = right = targetPos
            while left - 1 > -1 and nums[left - 1] == target:
                left -= 1
            while right + 1 < len(nums) and nums[right + 1] == target:
                right += 1
            return [left, right]