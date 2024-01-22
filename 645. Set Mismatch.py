class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        res = [0] * 2
        nums.sort()
        numsSet = set()
        for i in range(len(nums)):
            if nums[i] in numsSet:
                res[0] = nums[i]

            numsSet.add(nums[i])

            if i + 1 not in numsSet:
                res[1] = i + 1

        return res
