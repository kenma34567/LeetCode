class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        indexDict = dict()

        for i, num in enumerate(nums):
            if num in indexDict and abs(i - indexDict[num]) <= k:
                return True
            indexDict[num] = i

        return False
