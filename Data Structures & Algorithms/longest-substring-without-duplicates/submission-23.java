class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> maps = new HashMap<>();
        int max = 0;
        int l = 0;
        char[] arr = s.toCharArray();
        for(int r = 0; r < arr.length; ++r) {
            if (maps.containsKey(arr[r])) {
                l = Math.max(l, maps.get(arr[r]) + 1);
            }
            maps.put(arr[r], r);
            max = Math.max(max, r-l+1);
        }
        return max;
        
    }
}
