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

    private void bfs(TreeNode node) {
        if (node== null) {
            return;
        }
        bfs(node.left);
        arr.add(node.val);
        bfs(node.right);
    }
    public int kthSmallest(TreeNode root, int k) {
        arr = new ArrayList<>();
        bfs(root);

        return arr.get(k-1);
    }
}
