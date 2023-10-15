class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        def writeAns(nums: List[int], start: int, end: int):
            s = str(nums[start])
            if start != end:
                s = str(nums[start]) + "->" + str(nums[end])
            ans.append(s)

        if not nums:
            return []

        ans = []
        start = end = 0
        for i in range(1, len(nums)):

            prev = nums[i - 1]
            if nums[i] == prev + 1:
                end = i
                continue

            writeAns(nums, start, end)
            start = end = i

        # write for the last sorted list
        writeAns(nums, start, end)

        return ans
