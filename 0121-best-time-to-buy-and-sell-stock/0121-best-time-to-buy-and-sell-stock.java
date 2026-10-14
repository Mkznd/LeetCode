class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int minSoFar = prices[0];
        int profit = 0;

        for(int i=1;i<n;i++) {
            minSoFar = Math.min(minSoFar, prices[i]);
            profit = Math.max(profit, prices[i] - minSoFar);
        }

        return profit;
    }
}