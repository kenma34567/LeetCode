/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isEvenOddTree(TreeNode root) {
        if (root == null) return true;

        Queue<TreeNode> q = new ArrayDeque<TreeNode>();
        int level = 0;
        q.add(root);
        while (q.size() > 0) {
            int length = q.size();
            TreeNode prev = null;
            for (int i=0; i<length; i++) {
                TreeNode current = q.poll();
                //System.out.println("comparing " + level + " " + current.val);

                if (level % 2 != 0 &&
                    (current.val % 2 != 0 ||
                    (prev != null && current.val >= prev.val))) {        // odd
                    return false;
                } else if (level % 2 == 0 &&
                    (current.val % 2 == 0 ||
                    (prev != null && current.val <= prev.val))) {       // even
                    return false;
                }

                prev = current;
                if (current.left != null) q.add(current.left);
                if (current.right != null) q.add(current.right);
            }
            level++;
        }
        return true;
    }
}