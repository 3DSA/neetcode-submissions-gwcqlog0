class Solution {
    public boolean isAnagram(String s, String t) {
        int[] s_arr = new int[26];
        int[] t_arr = new int[26];
        for (char i: s.toCharArray()) {
            s_arr[(int)i - 97] += 1;
        }

        for (char i: t.toCharArray()) {
            t_arr[(int)i - 97] += 1;
        }
        return Arrays.equals(s_arr,t_arr);


    }
}
