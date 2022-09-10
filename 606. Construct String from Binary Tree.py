"""
Runtime: 121 ms Beats 12.38%
Memory: 22.5 MB Beats 5.63%
dfs
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def dfs(node: TreeNode, result: str) -> str:

            if not node:
                return result

            result += str(node.val)

            if node.left:
                result += "("
                result = dfs(node.left, result)
                result += ")"

            if node.right:
                if not node.left:
                    result += "()"
                result += "("
                result = dfs(node.right, result)
                result += ")"

            return result

        return dfs(root, "")
