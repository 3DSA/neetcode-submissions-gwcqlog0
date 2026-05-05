class Solution {
    public int maxProfit(int[] prices) {
        // sliding where the left would be left price, 
        // and we keep sliding and until we get to a lower price than the start, 
        // the left pointer becomes that
        int max_profit = 0;
        int left = prices[0];
        for (int price : prices) {
            if (left > price) {
                left = price;
            }
            max_profit = Math.max(max_profit, price-left);
        }
        return max_profit;
    }
}
