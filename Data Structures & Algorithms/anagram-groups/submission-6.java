class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> group = new HashMap<>();
        for (String word: strs) {
            int[] arr = new int[26];
            for (char s: word.toCharArray()) {
                arr[(int)s-97] += 1;
            }
            group.computeIfAbsent(Arrays.toString(arr), k -> new ArrayList<>()).add(word);
        }
        return new ArrayList<>(group.values());
    }
}
