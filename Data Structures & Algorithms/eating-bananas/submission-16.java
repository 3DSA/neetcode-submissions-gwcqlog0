class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        /*
        we go from 1 to the max of the amount of bananas in bile, and binary search through that
        calc hours for that
        */
        Arrays.sort(piles);
        int r = piles[piles.length-1];
        int max = r;
        int l = 1;
        while (l <= r) {
            int hours = 0;
            int rate = (l+r) / 2;
            for (int pile: piles) {
                hours += (int) Math.ceil((double) pile / rate);
            }
            if (hours > h) {
                l = rate+1;
            }
            else {
                r = rate-1;
            }
            if (hours <= h) {
                max = Math.min(max, rate);
            }
        }
        return max;
    }
}
