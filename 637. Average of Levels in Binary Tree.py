"""
Runtime: 84 ms Beats 53.24%
Memory: 17.2 MB Beats 10.32%
dfs
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        def dfs(node: TreeNode, level: int, levelDict: dict):

            if not node:
                return

            if level not in levelDict:
                levelDict[level] = []

            levelDict[level].append(node.val)

            if node.left:
                dfs(node.left, level+1, levelDict)

            if node.right:
                dfs(node.right, level+1, levelDict)

        levelDict = dict()
        dfs(root, 0, levelDict)

        result = [sum(levelList) / len(levelList) for levelList in levelDict.values()]

        print("RES", result)
        return result
