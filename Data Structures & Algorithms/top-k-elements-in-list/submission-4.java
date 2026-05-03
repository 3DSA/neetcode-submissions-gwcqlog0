class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // map = {}
        // for num in nums: map[num] +=1
        // 2d array where [[count, num] , [count, num]]
        Map<Integer, Integer> count = new HashMap<>();
        for(int num: nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }
        List<List<Integer>> arr = new ArrayList<>(); // This will be used to invert map and then sort
        count.forEach((num, total) -> {
            arr.add(List.of(total, num));
        });
        arr.sort((a, b) -> a.get(0) - b.get(0));
        int[] res = new int[k];
        for (int i = 0; i < k; ++i) {
            List<Integer> last = arr.remove(arr.size()-1);
            res[i] = last.get(1);
        }
        return res;
    }
}
