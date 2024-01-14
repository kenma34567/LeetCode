# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        pointer = head
        lastSwapped = None
        newHead = None
        while pointer:
            nodes = []
            for i in range(k):
                if pointer is None:
                    break
                nodes.append(pointer)
                pointer = pointer.next
                # print("NODE APPEND", nodes[i].val, pointer.val if pointer else "")
            if nodes and len(nodes) == k:
                if newHead is None:
                    newHead = nodes[-1]
                for i in range(len(nodes) - 1, 0, -1):
                    # print("reverse", nodes[i].val, nodes[i-1].val)
                    nodes[i].next = nodes[i - 1]
                if lastSwapped:
                    lastSwapped.next = nodes[-1]
                nodes[0].next = pointer
            lastSwapped = nodes[0]
            # print("check", nodes[0].val, pointer.val if pointer else "")

        return newHead
