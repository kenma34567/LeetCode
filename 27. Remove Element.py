class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        pointer = 0

        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = None
            else:
                if nums[pointer] == None:
                    nums[i], nums[pointer] = nums[pointer], nums[i]
                pointer += 1

        print("ans", nums)
        return pointer
