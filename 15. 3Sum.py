"""
Runtime: Beats 13.22%
Memory: Beats 5.72%
For-loop + Two-Pointers Solution
"""

class Solution:
    target = 0

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        # print("nums", nums)

        ansList = set()
        for i in range(len(nums) - 2):
            ''' Loop through the List and find ans for each pivot by 2-pointers'''
            left, right = i + 1, len(nums) - 1
            pivot = nums[i]

            result = nums[left] + pivot + nums[right]
            # print("doing pivot", nums[left], pivot, nums[right])

            ''' Pointers should run through whole list, then skip checking on same element until left => right'''
            while left < right:
                result = nums[left] + pivot + nums[right]
                if result < self.target:
                    ''' Check Left, if left collides with pivotIndex, additionally +1'''
                    left += 1
                    if left == i:
                        left += 1

                elif result > self.target:
                    ''' Check Right, if right collides with pivotIndex, additionally -1'''
                    right -= 1
                    if right == i:
                        right -= 1

                elif result == self.target:
                    self.addAnsToList(ansList, nums[left], pivot, nums[right])
                    if left == i - 1:
                        ''' if left reaches limit, move right, else default move left'''
                        right -= 1
                    else:
                        left += 1

        ansList = [list(ans) for ans in ansList]
        # print(ansList)
        return ansList

    def addAnsToList(self, ansList: List, leftNum: int, pivot: int, rightNum: int):
        ''' Dedup by using Set & Sorted Tuple'''
        # print("ADDING", leftNum, pivot, rightNum)
        listForSort = sorted([leftNum, pivot, rightNum])
        ansTuple = tuple(listForSort)
        ansList.add(ansTuple)

