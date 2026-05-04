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
    private void swap(TreeNode node) {
        if (node!= null) {
            TreeNode left = node.left;
            node.left = node.right;
            node.right = left;
            swap(node.left);
            swap(node.right);
        }
    }
    public TreeNode invertTree(TreeNode root) {
        swap(root);
        return root;
        
    }
}
