# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        def dfsAddNodeVal(sumTotal: int, node: Optional[TreeNode]):

            if not node.left and not node.right:
                return sumTotal + node.val == targetSum

            if node.left and dfsAddNodeVal(sumTotal + node.val, node.left):
                return True

            if node.right and dfsAddNodeVal(sumTotal + node.val, node.right):
                return True

            return False

        return dfsAddNodeVal(0, root)
