/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeZeroSumSublists(ListNode head) {
        int prefixSum = 0;
        ListNode start = new ListNode(0, head);
        ListNode current = head;
        Map<Integer, ListNode> sumToNode = new HashMap<>();
        sumToNode.put(0, start);
        while (current != null) {
            prefixSum += current.val;
            //System.out.println("prefixSum " + prefixSum);
            if (sumToNode.containsKey(prefixSum)) {
                //System.out.println("Hello ");
                ListNode prev = sumToNode.get(prefixSum);
                ListNode delete = prev.next;
                int sum = prefixSum;
                while (delete != current) {
                    //System.out.println("deleting " + delete.val);
                    sum += delete.val;
                    //System.out.println("removing " + sum);
                    sumToNode.remove(sum);
                    delete = delete.next;
                }
                prev.next = current.next;
            } else {
                sumToNode.put(prefixSum, current);
            }
            current = current.next;
        }

        return start.next;
    }

}