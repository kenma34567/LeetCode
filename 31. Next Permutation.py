class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        if n == 1:
            return
        elif n == 2:
            nums[0], nums[1] = nums[1], nums[0]
            return

        point = None

        # find the turning point
        for i in range(n - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                point = i - 1
                break

        if point is None:
            nums.sort()
            return

        # find the next larger index
        nextLargerIndex = None
        for i in range(n - 1, point, -1):
            if nums[i] <= nums[point]:
                continue
            if not nextLargerIndex:
                nextLargerIndex = i
            if nums[i] < nums[nextLargerIndex] and nums[i] > nums[point]:
                nextLargerIndex = i

        # swap
        print("Point", point, nextLargerIndex)
        nums[point], nums[nextLargerIndex] = nums[nextLargerIndex], nums[point]
        print(nums)

        # sort the remaining
        nums[point + 1:] = sorted(nums[point + 1:])
        print("final", nums)
