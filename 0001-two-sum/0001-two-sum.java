class Solution {
    public int[] twoSum(int[] nums, int target) {
        var a = new HashMap<Integer, Integer>();
        for(int i=0; i<nums.length; i++){
            if(a.containsKey(target-nums[i])){
                return new int[]{a.get(target-nums[i]), i};
            }
            a.put(nums[i], i);
        }
        return new int[]{0,0};
    }
}