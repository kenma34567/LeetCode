# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0, head)
        prev, current = temp, head

        while current and current.next:
            cnext = current.next
            cnext_next = current.next.next

            print("swapping", current.val, cnext.val)
            cnext.next = current  # the 2nd node becomes in front
            print("swapping2", prev.val, cnext.val)
            prev.next = cnext  # setting new "head" to be the 2nd node
            print("swapping3", current.val)
            current.next = cnext_next  # the 1st node now points to the 3rd node

            print("swapping4", current.val)
            prev = current  # shift to next part
            current = cnext_next  # shift to next part

        return temp.next
