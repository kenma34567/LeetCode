class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        x, y = 0, 0
        xLen, yLen = len(matrix[0]), len(matrix)
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])
        ans = []
        while len(ans) < xLen * yLen:

            print("check", right)
            for i in range(left, right):
                print("adding a", matrix[top][i])
                ans.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                print("adding b", matrix[i][right - 1])
                ans.append(matrix[i][right - 1])
            right -= 1

            if len(ans) == xLen * yLen:
                break

            for i in range(right - 1, left - 1, -1):
                print("adding c", right, left, matrix[bottom - 1][i])
                ans.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                print("adding d", matrix[i][left])
                ans.append(matrix[i][left])
            left += 1

        print("ans", ans)
        return ans
