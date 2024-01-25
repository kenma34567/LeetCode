# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:

        def possiblePalindrome(numCount: dict):
            if not numCount:
                return False

            count = sum(numCount.values())
            allowedSingle = 1 if count % 2 != 0 else 0
            singleCount = 0
            for count in numCount.values():
                if count % 2 != 0:
                    singleCount += 1
                if singleCount > allowedSingle:
                    return False

            return True

        def dfs(node: Optional[TreeNode], numCount: dict, ans: int):
            if not node:
                return ans

            numCount[node.val] = numCount.get(node.val, 0) + 1

            if node.left:
                ans = dfs(node.left, numCount.copy(), ans)
            if node.right:
                ans = dfs(node.right, numCount.copy(), ans)
            if not node.left and not node.right:
                # print("end", numCount)
                ans += 1 if possiblePalindrome(numCount) else 0

            return ans

        return dfs(root, {}, 0)
