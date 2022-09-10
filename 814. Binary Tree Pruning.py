"""
Runtime: 52 ms Beats 58.17%
Memory: 13.8 MB Beats 97.75%
dfs
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfsPruning(node: Optional[TreeNode]) -> Optional[TreeNode]:

            if not node:
                return None

            # if node.left:
            # print("running left", node)
            node.left = dfsPruning(node.left)

            # if node.right:
            # print("running right", node)
            node.right = dfsPruning(node.right)

            if node.val != 1 and not node.left and not node.right:
                return None

            return node

        # print("b4", root)
        root = dfsPruning(root)
        # print("CHECK", root)
        return root

