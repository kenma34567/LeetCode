"""
Runtime: 30 ms Beats 99.42%
Memory: 19.9 MB Beats 90.57%
dfs
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        """
            cal result for left and right respectively, return the max between max and min
        """

        def dfsCalMaxDif(node: Optional[TreeNode], maxVal: int, minVal: int):

            if not node:
                return maxVal - minVal

            # if node.val == 8:
            # print("return!", maxVal, minVal)

            minVal = min(minVal, node.val)
            maxVal = max(maxVal, node.val)

            leftResult = dfsCalMaxDif(node.left, maxVal, minVal)
            rightResult = dfsCalMaxDif(node.right, maxVal, minVal)

            return max(leftResult, rightResult)

        if not root:
            return 0

        return dfsCalMaxDif(root, root.val, root.val)

