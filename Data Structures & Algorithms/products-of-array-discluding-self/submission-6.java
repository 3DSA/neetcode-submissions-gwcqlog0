class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] res = new int[nums.length];
        int total = 1;
        for (int i = 0; i < nums.length; ++i) {
            res[i] = total;
            total *= nums[i];
        }
        total = 1;
        for (int i = nums.length-1; i > -1; --i) {
            res[i] *= total;
            total *= nums[i];
        }
        return res;
        
    }
}  
