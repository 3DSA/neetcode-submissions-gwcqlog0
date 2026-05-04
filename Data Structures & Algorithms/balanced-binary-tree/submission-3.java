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
    // we have a global indicator that is set to true, and if it becomes not balanced we set it false
    // we should use depth first search, and calc the left height then right height and if its uneven set to false
    private static boolean res;
    private int calc(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int left = calc(node.left);
        int right = calc(node.right);
        if (left-right < -1 || left-right > 1) {
            res = false;
        }
        return 1 + Math.max(left, right);
    }
    public boolean isBalanced(TreeNode root) {
        res = true;
        int temp = calc(root);
        return res;

    }
}
