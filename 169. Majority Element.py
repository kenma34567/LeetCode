class Solution:
def majorityElement(self, nums: List[int]) -> int:

    if len(nums) < 2:
        return nums[0]

    nums.sort()

    # print("nums", nums, len(nums)//2)

    counter = 1
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            counter += 1
        else:
            counter = 1

        if counter > len(nums) // 2:
            return nums[i]

    return None
