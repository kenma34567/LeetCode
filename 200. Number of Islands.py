class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ans = 0
        visited = set()

        def bfs(i, j):

            q = collections.deque()
            q.append((i, j))

            # top, bottom, left, right
            moveDir = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while q:
                current = q.popleft()
                visited.add(current)
                for move in moveDir:
                    moveI, moveJ = current[0] + move[0], current[1] + move[1]
                    if ((moveI, moveJ) not in visited and
                            moveI in range(len(grid)) and
                            moveJ in range(len(grid[moveI])) and
                            grid[moveI][moveJ] == "1"):
                        q.append((moveI, moveJ))
                        visited.add((moveI, moveJ))


        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfs(i, j)
                    ans += 1
                visited.add((i, j))

        return ans
