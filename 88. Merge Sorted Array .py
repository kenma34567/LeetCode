class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        pointerNums1, pointerNums2, pointerWrite = m - 1, n - 1, m + n - 1
        while pointerNums2 >= 0:
            print("comparing", nums1[pointerNums1], nums2[pointerNums2])

            if pointerNums1 >= 0 and nums1[pointerNums1] > nums2[pointerNums2]:
                print("writing pointer 1")
                nums1[pointerWrite] = nums1[pointerNums1]
                pointerNums1 -= 1
            else:
                print("writing pointer 2")
                nums1[pointerWrite] = nums2[pointerNums2]
                pointerNums2 -= 1
            pointerWrite -= 1

        print("ans", nums1)

