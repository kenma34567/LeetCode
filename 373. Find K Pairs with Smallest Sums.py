class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        h, ans = [], []

        for i, num in enumerate(nums1):
            heapq.heappush(h, (num + nums2[0], i, 0))

        while len(ans) < k:
            result, pos1, pos2 = heapq.heappop(h)  # pos1: index in nums1, pos2: index in nums2
            if pos2 < len(nums2) - 1:
                newRes = result - nums2[pos2] + nums2[pos2 + 1]  # num1 + new num2
                heapq.heappush(h, (newRes, pos1, pos2 + 1))
            ans.append([nums1[pos1], nums2[pos2]])

        return ans
