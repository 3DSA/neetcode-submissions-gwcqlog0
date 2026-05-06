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
    List<Integer> res;
    private void bfs(TreeNode node) {
        if (node == null) {
            return;
        }
        bfs(node.left);
        res.add(node.val);
        bfs(node.right);
    }
    public boolean isValidBST(TreeNode root) {
        res = new ArrayList<>();
        int prev = -1001;
        bfs(root);
        for (int num: res) {
            if (num <= prev) {
                return false;
            }
            prev = num;
        }
        return true;
    }
}
