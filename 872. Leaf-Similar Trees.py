"""
Runtime: 39 ms Beats 77.56%
Memory: 13.8 MB Beats 89.21%
dfs
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        """
            dfs to find all leafValues, then compare 2 lists
        """
        def dfs(root: Optional[TreeNode], leafValues: List) -> List:

            if not root:
                return leafValues

            if root.left:
                dfs(root.left, leafValues)

            if root.right:
                dfs(root.right, leafValues)

            if not root.left and not root.right:
                leafValues.append(root.val)

            return leafValues

        list1 = dfs(root1, [])
        list2 = dfs(root2, [])

        print("COMPARE", list1, list2)
        return list1 == list2