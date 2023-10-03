class Solution:

    def reverseInPlace(self, l: List[int], start: int, end: int) -> None:

        while end > start:
            l[start], l[end] = l[end], l[start]
            start, end = start + 1, end - 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        Approach:   1) from k, find out the final position of the 1st element, which is 0 + k%len(nums)
                    2) reverse the order of nums
                    3) reverse nums again, for the first half of nums, which is, [0:0+k%len(nums)]
                    4) reverse the remaining part of nums
        """

        if len(nums) < 2:
            return

        finalPosition = k % len(nums)

        nums.reverse()
        # print("ID", id(nums))
        self.reverseInPlace(nums, 0, finalPosition - 1)
        self.reverseInPlace(nums, finalPosition, len(nums) - 1)
        # print("final", nums, id(nums))
