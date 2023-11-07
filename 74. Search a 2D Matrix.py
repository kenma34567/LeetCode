class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = left + (right - left) // 2
            midX, midY = mid % n, mid // n
            # print("mid", left, right, mid, midX, midY)

            midNum = matrix[midY][midX]
            # print("mid num", midNum)
            if midNum == target:
                return True
            elif midNum > target:
                right = mid - 1
            elif midNum < target:
                left = mid + 1

        return False
