class Solution {
    Set<List<Integer>> res;

    private void compute(int[] nums, int index, Deque<Integer> curr) {
        if (index == nums.length) {
            res.add(new ArrayList<>(curr));
            return;
        }
        curr.push(nums[index]);
        compute(nums, index+1, curr);
        curr.pop();
        compute(nums, index+1, curr);
    }
    public List<List<Integer>> subsets(int[] nums) {
       // sort of a decision tree
       res = new HashSet<>();
       Deque<Integer> queue = new ArrayDeque<>();
       compute(nums, 0, queue);
       return new ArrayList<>(res);
    }
}
