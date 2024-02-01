class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans, subArr = [], []
        for i in range(len(nums)):
            if not subArr or nums[i] - subArr[0] <= k:
                subArr.append(nums[i])
            elif nums[i] - subArr[0] > k:
                return []

            if len(subArr) == 3:
                ans.append(subArr)
                subArr = []

        return ans
