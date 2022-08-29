"""
Runtime: 477 ms Beats 97.90%
Memory: 15.3 MB Beats 17.94%
Dynamic Programming + greedy
"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:

        minIndex = len(nums) - 1  # min index in nums that can reach the end, default = last element
        # reachableIndexSet = set([len(nums)-1]) # indexes that can reach the end

        for i in range(len(nums) - 1, -1, -1):

            # print("check Set", reachableIndexSet)
            reachable = i + nums[i] >= minIndex
            # print("reachable?", i)
            if reachable:
                # reachableIndexSet.add(i)
                minIndex = i  # loop from the end, minIndex must be updated if reachable
                if i == 0:
                    return True

        return False
