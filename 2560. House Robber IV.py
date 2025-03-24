class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        '''
            binary search -> search space to be min(nums) -> max(nums)
                every time, choose mid as the capability and check if it is enough to rob k houses:
                    for each nums, if n < mid, rob that house and add robbed_count
                    if robbed_count >= k -> we can try to reduce the capability to see if it is still enough
                    until not enough / left == right, then return
        '''

        def checkEnoughCapability(mid):
            index = 0
            robbed_count = 0
            while index < len(nums):
                if nums[index] <= mid:
                    robbed_count += 1
                    index += 2
                else:
                    index += 1
            # print("check enough", mid, robbed_count)
            return robbed_count >= k

        left, right = min(nums), max(nums)

        while left < right:
            mid = (left + right) // 2
            if checkEnoughCapability(mid):
                right = mid
            else:
                left = mid + 1

        return left
