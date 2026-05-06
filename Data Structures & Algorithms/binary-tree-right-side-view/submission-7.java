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
    public List<Integer> rightSideView(TreeNode root) {
        Deque<TreeNode> queue = new ArrayDeque<>();
        List<Integer> res = new ArrayList<>();
        if (root == null) {
            return res;
        }
        queue.offer(root);
        int i;
        TreeNode node;
        int size;
        while (!queue.isEmpty()) {
            size = queue.size();
            for (i = 0; i < size; ++i) {
                node = queue.poll();
                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
                if (i == size-1) {
                    res.add(node.val);
                }
            }
        }
        return res;
        
    }
}
