"""
Runtime: 52 ms Beats 55.32%
Memory: 14.2 MB Beats 72.95%
dfs + dict of dict solution
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import bisect


class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        def dfs(node: TreeNode, rowIndex: int, columnIndex: int, indexDict: dict(dict())) -> dict:

            if not node:
                return indexDict

            # print("processing", node.val, indexDict)

            if columnIndex not in indexDict:
                indexDict[columnIndex] = dict()
            if rowIndex not in indexDict[columnIndex]:
                indexDict[columnIndex][rowIndex] = []
            bisect.insort_left(indexDict[columnIndex][rowIndex], node.val)

            if node.left:
                indexDict = dfs(node.left, rowIndex + 1, columnIndex - 1, indexDict)

            if node.right:
                indexDict = dfs(node.right, rowIndex + 1, columnIndex + 1, indexDict)

            return indexDict

        indexDict = dfs(root, 0, 0, dict(dict()))

        result = []
        sortedColumnKeys = sorted(indexDict.keys())
        for i in sortedColumnKeys:
            resultElement = []
            sortedRowKeys = sorted(indexDict[i].keys())
            for j in sortedRowKeys:
                resultElement.extend(indexDict[i][j])
            result.append(resultElement)

        return result
