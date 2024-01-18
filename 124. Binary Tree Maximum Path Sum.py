# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = float("-inf")

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0

            # print("processing", node.val)
            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            current = node.val
            self.ans = max(self.ans, current, leftMax + current, rightMax + current, leftMax + current + rightMax)

            return max(leftMax + current, current + rightMax, current)

        dfs(root)
        return self.ans
