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
    private static int max = 0;
    private int calc(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int left = calc(node.left);
        int right = calc(node.right);
        max = Math.max(max, left + right);
        return 1 + Math.max(left, right);
    }
    public int diameterOfBinaryTree(TreeNode root) {
        max = 0;
        int temp = calc(root);
        return max;
    }
}
