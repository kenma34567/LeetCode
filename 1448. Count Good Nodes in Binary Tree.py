"""
Runtime: 518 ms Beats 12.88%
Memory: 32.5 MB Beats 87.02%
Simple dfs solution
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def checkGood(node: TreeNode, maxVal: int, count: int) -> int:

            if not node:
                return count

            if node.val >= maxVal:
                maxVal = node.val
                count += 1

            # print("checking", node.val, maxVal, count)

            # check left
            count = checkGood(node.left, maxVal, count)
            # check right
            count = checkGood(node.right, maxVal, count)

            return count

        count = checkGood(root, root.val, 0)
        return count
