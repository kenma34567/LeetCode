"""
Runtime: 104 ms Beats 16.00%
Memory: 16.2 MB Beats 10.90%
bfs
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        def treeTraversal(node: 'Node', resultDict: dict, level: int) -> dict:

            if not node:
                return resultDict

            if node.children:
                sameLevelNodes = []
                if level in resultDict:
                    sameLevelNodes = resultDict[level]
                sameLevelNodes.extend([child.val for child in node.children if child is not None])
                if len(sameLevelNodes) > 0:
                    resultDict[level] = sameLevelNodes

                for child in node.children:
                    resultDict = treeTraversal(child, resultDict, level + 1)

            return resultDict

        dummyRoot = Node(val=None, children=[root])
        resultDict = treeTraversal(dummyRoot, dict(), 0)
        print("result Dict", resultDict)

        result = []
        for key in sorted(resultDict.keys()):
            result.append(resultDict[key])

        return result
