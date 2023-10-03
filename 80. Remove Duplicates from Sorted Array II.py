class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        pointer = 2

        for i in range(2, len(nums)):
            print("index", i, pointer)
            if nums[i] != nums[pointer - 2]:
                nums[pointer] = nums[i]
                pointer += 1

        print("nums", nums)
        return pointer