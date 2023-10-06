class Solution:
    def jump(self, nums: List[int]) -> int:

        """
            1) Find out the reachable window of currenrt index (must start with maxReachable + 1)
            2) Loop until we reach the last element
        """

        if len(nums) < 2:
            return 0

        left, right = 0, 0
        maxReachable = 0
        jumps = 0

        while right < len(nums) - 1:

            for i in range(left, right + 1):
                maxReachable = max(maxReachable, i + nums[i])

            left = right + 1
            right = maxReachable
            jumps += 1

        # print("jumps", jumps)
        return jumps
