"""
Runtime: Beats 98.4%
Memory: Beats 21.1%
Modified Binary Search For "flipped" nums
"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def doRotated(nums: List[int], target: int, left: int, right: int) -> int:

            while left < right:

                mid = left + ((right - left) // 2)

                print("checking", left, mid, right)

                if nums[left] == target:
                    return left
                elif nums[right] == target:
                    return right
                elif nums[mid] == target:
                    return mid

                if left == mid or right == mid:
                    break

                """
                    Use the left-half when
                        1) target is within range of left & mid [4,5,6,1,2] find 5
                        2) left > mid and target > left         [7,8,1,2,3] find 8
                        3) mid > left and left > target         [5,1,2,3,4] find 1
                """
                if nums[mid] > target > nums[left] or target > nums[left] > nums[mid] or nums[left] > nums[
                    mid] > target:
                    right = mid
                else:
                    left = mid

            return -1

        def doBinarySearch(nums: List[int], target: int, left: int, right: int) -> int:

            while left < right:

                mid = left + ((right - left) // 2)

                if nums[left] == target:
                    return left
                elif nums[right] == target:
                    return right
                elif nums[mid] == target:
                    return mid

                if left == mid or right == mid:
                    break

                if nums[mid] > target:
                    right = mid
                else:
                    left = mid

            return -1

        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        elif len(nums) == 2:
            if nums[0] == target:
                return 0
            elif nums[1] == target:
                return 1
            else:
                return -1

        left, right = 0, len(nums) - 1
        mid = left + ((right - left) // 2)

        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right
        elif nums[mid] == target:
            return mid

        rotated = nums[right] < nums[left]
        print("nn", rotated)

        if rotated:
            print("do rotated", left, right)
            return doRotated(nums, target, left, right)
        else:
            print("do normal")
            return doBinarySearch(nums, target, left, right)
