class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> maps = new HashMap<>();
        for (int i = 0; i < nums.length; ++i) {
            maps.put(target-nums[i], i);
        }
        for (int i = 0; i < nums.length; ++i) {
            if (maps.containsKey(nums[i])) {
                if (maps.get(nums[i]) != i) {
                    return new int[]{i, maps.get(nums[i])};

                }
            }
        }
        return new int[]{-1,-1};

    }
}
