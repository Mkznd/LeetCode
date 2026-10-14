class Solution {
    public int maxProfit(int[] prices) {
        int n = prices.length;
        int[] mins = new int[n];
        int profit = 0;

        mins[0] = prices[0];
        for(int i=1;i<n;i++) {
            mins[i] = Math.min(mins[i-1], prices[i]);
        }

        for(int i=0;i<n;i++) {
            profit = Math.max(profit, prices[i]-mins[i]);
        }

        return profit >= 0 ? profit : 0;
        
    }
}