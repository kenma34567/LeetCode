class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        visited = set()

        def bfs(i, j):
            q = collections.deque()
            q.append((i, j))
            remove = set()
            remove.add((i, j))
            shouldRemove = True

            # top, bottom, left, right
            moveDir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            while q:
                current = q.popleft()
                visited.add(current)
                for move in moveDir:
                    moveI, moveJ = current[0] + move[0], current[1] + move[1]
                    if (moveI in range(len(board)) and
                            moveJ in range(len(board[i])) and
                            board[moveI][moveJ] == "O" and
                            (moveI, moveJ) not in visited):
                        remove.add((moveI, moveJ))
                        q.append((moveI, moveJ))
                        visited.add((moveI, moveJ))
                    elif (moveI not in range(len(board)) or
                          moveJ not in range(len(board[i]))):
                        shouldRemove = False

            if shouldRemove:
                for r in remove:
                    rI, rJ = r[0], r[1]
                    board[rI][rJ] = "X"

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "O" and (i, j) not in visited:
                    bfs(i, j)
                visited.add((i, j))
