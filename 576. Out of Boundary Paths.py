class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        MOD = 10 ** 9 + 7
        cache = {}

        def dfs(i: int, j: int, moves: int):
            # print("processing", i, j)
            if (i < 0 or i == m or j < 0 or j == n):
                # print("im at", i, j)
                return 1
            if moves == 0:
                return 0
            if (i, j, moves) in cache:
                return cache[(i, j, moves)]

            ans = 0
            # top, bottom, left, right
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for d in directions:
                ans += dfs(i + d[0], j + d[1], moves - 1) % MOD
            cache[(i, j, moves)] = ans % MOD

            return cache[(i, j, moves)]

        return dfs(startRow, startColumn, maxMove)
