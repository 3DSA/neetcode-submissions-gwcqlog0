class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> window = new HashMap<>();
        int l = 0;
        int max = 0;
        char [] arr = s.toCharArray();
        for (int r = 0; r < arr.length; ++r) {
            if (window.containsKey(arr[r])) {
                l = Math.max(l, window.get(arr[r]) + 1);
            }
            window.put(arr[r], r);
            max = Math.max(max, r-l+1);
        }
        return max;

    }
}
