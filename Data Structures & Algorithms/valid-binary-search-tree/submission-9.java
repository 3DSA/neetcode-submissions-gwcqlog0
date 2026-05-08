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
    List<Integer> arr;

    private void compute(TreeNode node) {
        if (node == null) {
            return;
        }
        compute(node.left);
        arr.add(node.val);
        compute(node.right);
    }
    public boolean isValidBST(TreeNode root) {
        arr = new ArrayList<>();
        compute(root); // in order traversal
        int prev = -1001;
        for (int val : arr) {
            if (val <= prev) {
                return false;
            }
            prev = val;
        }
        return true;

    }
}
