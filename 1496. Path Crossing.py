class Solution:
    def isPathCrossing(self, path: str) -> bool:

        def walk(current, direction):

            if direction == "N":
                current[1] += 1
            elif direction == "S":
                current[1] -= 1
            elif direction == "E":
                current[0] += 1
            elif direction == "W":
                current[0] -= 1

            return current

        current = [0, 0]
        visited = dict()  # key = x, value = set of y
        visited[0] = {0}
        for d in path:
            current = walk(current, d)
            visited[current[0]] = visited.get(current[0], set())
            if current[1] in visited[current[0]]:
                return True
            visited[current[0]].add(current[1])

        return False
