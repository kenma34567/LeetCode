"""
Runtime: 50 ms Beats 75.97%
Memory: 16.5 MB Beats 78.57%
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """
            @param head = odd head, odd = pointer to traverse odd
            @param evenHead = even head, even = point to traverse even
            lastly, odd.next = evenHead to link the 2 linked list
        """

        if not head:
            return None

        odd = head
        even = evenHead = head.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = evenHead
        return head