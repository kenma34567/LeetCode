class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        pointer = 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                # print("change detected", i, pointer)
                pointer += 1
                nums[pointer] = nums[i]

        return pointer + 1
