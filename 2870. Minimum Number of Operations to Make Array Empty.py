class Solution:
    def minOperations(self, nums: List[int]) -> int:

        numCount = Counter(nums)
        count = 0

        for k, v in numCount.items():
            while v > 1:
                if v % 3 == 0:
                    count += 1
                    v -= 3
                elif v % 2 == 0:
                    count += 1
                    v -= 2
                else:
                    count += 1
                    v -= 3
            if v == 1:
                return -1

        return count
