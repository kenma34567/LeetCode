class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right-left)//2
            print("mid index", mid)

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                if nums[mid] < target or target < nums[left]:
                    left = mid+1
                else:
                    right = mid-1
            else:
                if target < nums[mid] or nums[right] < target:
                    right = mid-1
                else:
                    left = mid+1


        return -1


        '''
            [4,5,6,7,8,0,1,2], target = 8
            [1,2,3,4,5,6], target = 4
        '''
