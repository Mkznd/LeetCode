class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = HashSet.newHashSet(nums.length);
        for (int x : nums) set.add(x);

        int maxLen = 0;
        var curLen = 0;
        var curElement = 0;
        for(var i: set){
            curLen = 0;
            curElement = i;
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