# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def dfs(node: Optional[TreeNode], seq: []):
            if not node:
                return seq

            if not node.left and not node.right:
                seq.append(node.val)

            seq = dfs(node.left, seq)
            seq = dfs(node.right, seq)

            return seq

        return dfs(root1, []) == dfs(root2, [])
