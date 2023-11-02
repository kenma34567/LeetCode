# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        def bfs(root: Optional[TreeNode], levelList: List[int], level: int) -> List[int]:

            if not root:
                return []

            # print("im now at", root.val, level)
            if level > len(levelList) - 1:
                levelList.append(root.val)

            if root.right:
                bfs(root.right, levelList, level + 1)
            if root.left:
                bfs(root.left, levelList, level + 1)

            return levelList

        levelList = bfs(root, [], 0)
        print("CC", levelList)
        return levelList
