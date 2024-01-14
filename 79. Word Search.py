class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtrack(pointer: int, i: int, j: int, used: set()) -> bool:
            if pointer >= len(word):
                return True

            ans = False
            # top bottom left right
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for d in directions:
                movedI, movedJ = i + d[0], j + d[1]
                if movedI not in range(len(board)) or movedJ not in range(len(board[i])):
                    continue
                if (movedI, movedJ) in used:
                    continue
                current = board[movedI][movedJ]

                if current == word[pointer]:
                    used.add((movedI, movedJ))
                    ans = backtrack(pointer + 1, movedI, movedJ, used)
                    if ans:
                        return ans
                    else:
                        used.remove((movedI, movedJ))

            return ans

        pointer = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                char = board[i][j]
                if char == word[pointer]:
                    used = set()
                    used.add((i, j))
                    ans = backtrack(pointer + 1, i, j, used)
                    if ans:
                        return True

                    used.remove((i, j))

        return False
