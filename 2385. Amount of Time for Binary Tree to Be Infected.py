# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        def setAdjacentBFS(root: Optional[TreeNode], adjacentDict: dict):
            q = collections.deque()
            q.append(root)
            while q:
                node = q.popleft()
                adjacentDict[node.val] = adjacentDict.get(node.val, [])
                if node.left:
                    q.append(node.left)
                    adjacentDict[node.val].append(node.left.val)
                    adjacentDict[node.left.val] = adjacentDict.get(node.left.val, [])
                    adjacentDict[node.left.val].append(node.val)
                if node.right:
                    q.append(node.right)
                    adjacentDict[node.val].append(node.right.val)
                    adjacentDict[node.right.val] = adjacentDict.get(node.right.val, [])
                    adjacentDict[node.right.val].append(node.val)

            return adjacentDict

        def calDistanceFromStartToNodes(adjacentDict: dict, distanceDict: dict):
            q = collections.deque()
            q.append(start)
            distanceDict[start] = 0
            visited = set()
            while q:
                val = q.popleft()
                adjs = adjacentDict[val]
                for adj in adjs:
                    if adj in visited:
                        continue
                    distanceDict[adj] = distanceDict.get(val, 0) + 1
                    q.append(adj)
                visited.add(val)

            return distanceDict

        adjacentDict = setAdjacentBFS(root, {})
        distanceDict = calDistanceFromStartToNodes(adjacentDict, {})

        return max(distanceDict.values())
