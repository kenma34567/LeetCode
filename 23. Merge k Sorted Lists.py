"""
Simple solution using min heap
Runtime: Beats 36.37%
Memory: Beats 28.26%
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        min_heap = []
        ans = ListNode()
        for i in range(len(lists)):
            head = lists[i]
            while head:
                heapq.heappush(min_heap, head.val)
                head = head.next

        print("CCC", min_heap)

        current = ans
        while min_heap:
            v = heapq.heappop(min_heap)
            current.next = ListNode(val=v)
            print("test pop", v)
            current = current.next

        return ans.next



