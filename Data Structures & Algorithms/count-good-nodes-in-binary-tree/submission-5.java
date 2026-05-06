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
    int res;
    private void dfs(TreeNode node, int val) {
        if (node == null) {
            return;
        }
        if (node.val >= val) {
            res += 1;
        }
        dfs(node.left, Math.max(node.val, val));
        dfs(node.right, Math.max(node.val, val));

    }
    public int goodNodes(TreeNode root) {
        res = 0;
        dfs(root, -101);
        return res;
    }
}
