# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None

        root = TreeNode(val=preorder[0])
        rootIndexInOrder = inorder.index(preorder[0])
        print("root index", rootIndexInOrder)

        '''
            1) preorder[0] is root val
            2) elements on the left of root val in inorder is in the left-subtree (also for right)

        '''

        leftPreOrder = preorder[1:rootIndexInOrder + 1]
        leftInOrder = inorder[0:rootIndexInOrder]
        root.left = self.buildTree(leftPreOrder, leftInOrder)

        rightPreOrder = preorder[rootIndexInOrder + 1:]
        rightInOrder = inorder[rootIndexInOrder + 1:]
        root.right = self.buildTree(rightPreOrder, rightInOrder)

        return root