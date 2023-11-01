"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        copyDict = {None: None}
        pointer = head
        while pointer:
            copyDict[pointer] = Node(x=pointer.val)
            pointer = pointer.next

        pointer = head
        while pointer:
            headCopy = copyDict[pointer]
            headCopy.next = copyDict[pointer.next]
            headCopy.random = copyDict[pointer.random]
            pointer = pointer.next

        return copyDict[head]