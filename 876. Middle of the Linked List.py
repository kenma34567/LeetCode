"""
Runtime: 34 ms Beats 79.61%
Memory: 13.7 MB Beats 96.9%
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
            fast travels 2-times fast then slow
            when fast reaches the end, slow = middle
        """
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
