class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        cache = {}

        def dfs(i: int, j: int):
            num = matrix[i][j]
            if i == len(matrix) - 1:
                return num
            if (i, j) in cache:
                return cache[(i, j)]

            directions = [(1, -1), (1, 0), (1, 1)]
            currentSum = float("inf")
            for d in directions:
                movedI, movedJ = i + d[0], j + d[1]
                if (movedI not in range(len(matrix)) or
                        movedJ not in range(len(matrix[movedI]))):
                    continue

                # print("pass", i, j, num)
                currentSum = min(num + dfs(movedI, movedJ), currentSum)
                # print("answer?", i, j, currentSum)

            cache[(i, j)] = currentSum
            return currentSum

        ans = float("inf")
        for j in range(len(matrix[0])):
            ans = min(ans, dfs(0, j))
        return ans
