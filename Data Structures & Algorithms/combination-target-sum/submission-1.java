class Solution {
    Set<List<Integer>> res;
    private void compute(int[] nums, int sum, int index, int target, List<Integer> curr) {
        if (sum == target) {
            res.add(List.copyOf(curr));
            return;
        }
        if (index >= nums.length || sum > target) {
            return;
        }
        curr.add(nums[index]);
        compute(nums, sum+nums[index], index, target, curr);
        curr.remove(curr.size()-1);
        compute(nums, sum, index+1, target, curr);

    }
    public List<List<Integer>> combinationSum(int[] nums, int target) {
        res = new HashSet<>();
        List<Integer> curr = new ArrayList<>();
        compute(nums, 0, 0, target, curr);
        return new ArrayList<>(res);

    }
}
