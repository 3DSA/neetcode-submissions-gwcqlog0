class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num: nums) {
            set.add(num);
        }
        int longest_sequence = 0;
        int sequence;
        for (int num: nums) {
            sequence = 0;
            if(!set.contains(num-1)) {
                while (set.contains(num)) {
                    sequence += 1;
                    num +=1;
                }
            longest_sequence = Math.max(longest_sequence, sequence);
            }
        }
        return longest_sequence;
    }
}
