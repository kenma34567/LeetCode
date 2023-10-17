class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        """
            Write from the end, use 2 pointers to compare element and write the larger one
            If one of the array has run out of elements, write the remaining of the other
        """

        m, n = len(nums1) - len(nums2), len(nums2)
        pNums1, pNums2, pWrite = m - 1, n - 1, m + n - 1

        while pWrite > -1:

            if pNums1 < 0 or (pNums2 > -1 and nums2[pNums2] >= nums1[pNums1]):
                # print("writing 2", nums2[pNums2], pWrite)
                nums1[pWrite] = nums2[pNums2]
                pNums2 -= 1
            else:
                # print("writing 1", pNums1)
                nums1[pWrite] = nums1[pNums1]
                pNums1 -= 1

            pWrite -= 1

        print("ans", nums1)
