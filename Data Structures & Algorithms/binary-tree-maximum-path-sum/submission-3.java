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
    int max;
    private int compute(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int left = compute(node.left);
        int right = compute(node.right);
        int curr = Math.max( node.val + Math.max(left, right), Math.max(node.val, node.val + left + right));
        max = Math.max(curr, max);
        return Math.max(node.val, node.val + Math.max(left, right));
    }
    public int maxPathSum(TreeNode root) {
        max = -1001;
        compute(root);
        return max;
        
    }
}
