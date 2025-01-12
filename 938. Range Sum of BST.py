"""
Runtime: 253 ms Beats 78.57%
Memory: 23 MB Beats 50.13%
bfs
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        if not root:
            return 0

        def BFS(root: Optional[TreeNode], low: int, high: int, ans: int) -> int:

            if low <= root.val <= high:
                print("adding", root.val)
                ans += root.val

            if root.left:
                ans = BFS(root.left, low, high, ans)

            if root.right:
                ans = BFS(root.right, low, high, ans)
            return ans

        return BFS(root, low, high, 0)




