"""
Runtime: Beats 7.17%
Memory: Beats 43.30%
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def count_list_size(self, l: ListNode) -> int:

        len_l = 1
        while l.next:
            len_l += 1
            l = l.next
        return len_l

    def carry_add(self, sum: int, carry: bool) -> int:

        if carry:
            sum += 1
            carry = False
        if sum >= 10:
            carry = True
            sum -= 10

        return sum, carry

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        len_l1 = self.count_list_size(l1)
        len_l2 = self.count_list_size(l2)

        size = max(len_l1, len_l2)
        result = None
        previous_node = None
        carry = False
        print("size", size)
        print("l1, l2", l1, l2)

        for i in range(size + 1):

            sum = -1
            if l1 and l2:
                sum = l1.val + l2.val
                print("sum?", sum)
                sum, carry = self.carry_add(sum, carry)
                l1 = l1.next
                l2 = l2.next
            elif l1:
                sum = l1.val
                sum, carry = self.carry_add(sum, carry)
                l1 = l1.next
            elif l2:
                sum = l2.val
                sum, carry = self.carry_add(sum, carry)
                l2 = l2.next
            else:
                print("last!")
                if carry:
                    sum = 1
                    carry = False
                # sum, carry = self.carry_add(sum, carry)

            if sum > -1:
                if not result:
                    result = ListNode(sum)
                    previous_node = result
                else:
                    temp_node = ListNode(sum)
                    previous_node.next = temp_node
                    previous_node = temp_node

        return result


