class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> dupes = new HashSet<>();
        for(int num: nums) {
            if (dupes.contains(num)) {
                return true;
            }
            dupes.add(num);
        }
        return false;

        
    }
}