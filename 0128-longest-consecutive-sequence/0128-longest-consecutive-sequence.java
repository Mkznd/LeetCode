class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>(nums.length);
        for (int x : nums) set.add(x);

        int maxLen = 0;

        for(var i: set){
            var curLen = 0;
            var curElement = i;

            if (set.contains(curElement+1)) continue;
            while(set.contains(curElement)){
                curLen++;
                curElement--;
            }
            maxLen = Math.max(maxLen, curLen);
        }

        return maxLen;
    }
}