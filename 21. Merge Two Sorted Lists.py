# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1

        ans = ListNode()  # head
        temp = ans

        if list1.val > list2.val:
            ans.next = list1
        else:
            ans.next = list2

        while list1 and list2:

            if list1.val > list2.val:
                temp.next = list2
                list2 = list2.next
                temp = temp.next
            else:
                temp.next = list1
                list1 = list1.next
                temp = temp.next

        if not list1:
            temp.next = list2
        elif not list2:
            temp.next = list1

        print("AMNS", ans)

        return ans.next
