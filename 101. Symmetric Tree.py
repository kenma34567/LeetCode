# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isSubSymmetric(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:

            if left == right is None:
                return True

            if left is None and right:
                return False

            if left and right is None:
                return False

            if left.val != right.val:
                return False

            if left.left or left.right or right.left or right.right:
                return isSubSymmetric(left.left, right.right) and isSubSymmetric(left.right, right.left)

            return True

        return isSubSymmetric(root.left, root.right)
