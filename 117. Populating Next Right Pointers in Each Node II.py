"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return None

        q = collections.deque([root])
        while q:
            qLen = len(q)

            prevNode = None
            # print("q", [x.val if x else "" for x in q])
            for i in range(qLen):
                node = q.popleft()
                if prevNode:
                    prevNode.next = node

                if node and node.left:
                    q.append(node.left)
                if node and node.right:
                    q.append(node.right)

                prevNode = node

        return root



