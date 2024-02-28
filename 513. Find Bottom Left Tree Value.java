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
    public int findBottomLeftValue(TreeNode root) {
        return bfs(root);
    }

    private int bfs(TreeNode node) {
        TreeNode leftmost = node;
        Queue<TreeNode> q = new ArrayDeque<TreeNode>();
        q.add(node);
        while (q.size() > 0) {
            leftmost = q.peek();
            int length = q.size();
            for (int i=0; i<length; i++) {
                TreeNode current = q.poll();
                if (current.left != null) q.add(current.left);
                if (current.right != null) q.add(current.right);
            }
        }

        return leftmost.val;
    }
}