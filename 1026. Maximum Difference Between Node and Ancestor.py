# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], maxAbsAncestor: int, minAbsAncestor: int, ans: int):
            if not node:
                return ans

            # print("processing", node.val, "max", maxAbsAncestor, "min", minAbsAncestor)

            maxAbsAncestor = max(maxAbsAncestor, node.val)
            minAbsAncestor = min(minAbsAncestor, node.val)
            ans = max(ans, maxAbsAncestor - minAbsAncestor)

            ans = dfs(node.left, maxAbsAncestor, minAbsAncestor, ans)
            ans = dfs(node.right, maxAbsAncestor, minAbsAncestor, ans)

            return ans

        ans = dfs(root, root.val, root.val, 0)
        return ans
