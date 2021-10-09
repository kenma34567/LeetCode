"""
Runtime: Beats 72.96%
Memory: Beats 97.85%
"""


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()
        ans = set()

        for i in range(len(nums)):
            num1 = nums[i]
            if target < 4 * num1:
                break
            for j in range(i + 1, len(nums)):
                num2 = nums[j]
                if num1 + 3 * num2 > target:
                    break

                left = j + 1
                right = len(nums) - 1

                while left < right:

                    num3 = nums[left]
                    num4 = nums[right]

                    if num1 + num2 + 2 * num3 > target:
                        break
                    if num1 + num2 + 2 * num4 < target:
                        break

                    sum_result = num1 + num2 + num3 + num4
                    if sum_result == target:
                        ans.add((num1, num2, num3, num4))
                        left += 1
                        right -= 1
                    elif sum_result < target:
                        left += 1
                    elif sum_result > target:
                        right -= 1

        return ans