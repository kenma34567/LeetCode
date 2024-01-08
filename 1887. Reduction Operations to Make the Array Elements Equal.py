class Solution:
    def reductionOperations(self, nums: List[int]) -> int:

        """
            if num != smallest, find the "difference" between num and smallest,
            where "difference" means no. of distinct elements between num and smallest in the list

            sort the list first so that the "difference" can remain the same
        """

        nums.sort()
        smallest = currentNum = nums[0]
        diff = 0
        print("sorted", nums)

        counter = 0
        for i, num in enumerate(nums):
            if num == smallest:
                continue

            if num != currentNum:
                currentNum = num
                diff += 1

            counter += diff

        return counter
