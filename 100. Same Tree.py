# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def bfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

            if p == q is None:
                return True

            if p and q is None:
                return False

            if p is None and q:
                return False

            print("comparing", p.val, q.val)

            if p.left and q.left is None:
                return False

            if p.left is None and q.left:
                return False

            if p.right and q.right is None:
                return False

            if p.right is None and q.right:
                return False

            if p.val != q.val:
                return False

            resultLeft = resultRight = True
            if p.left:
                resultLeft = bfs(p.left, q.left)

            if p.right:
                resultRight = bfs(p.right, q.right)

            return resultLeft and resultRight

        return bfs(p, q)
