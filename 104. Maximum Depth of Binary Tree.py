# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0

        def transverse(root: Optional[TreeNode], depth: int) -> int:

            depth += 1
            maxDepth = depth
            print("trans", root.val, depth)
            if root.left == root.right is None:
                return maxDepth

            depthLeft = maxDepth
            if root.left:
                depthLeft = transverse(root.left, depthLeft)

            depthRight = maxDepth
            if root.right:
                depthRight = transverse(root.right, depthRight)

            maxDepth = max(depthLeft, depthRight)
            return maxDepth

        maxDepth = transverse(root, 0)
        print("CC", maxDepth)
        return maxDepth