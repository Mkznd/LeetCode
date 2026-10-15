class Solution {
    public Set<List<Integer>> twoSum(int[] nums, int target){
        Set<List<Integer>> result = new HashSet<List<Integer>>();
        Map<Integer, Integer> map = new HashMap<>();

        for(int i=0;i<nums.length;i++){
            if(map.containsKey(target-nums[i])){
                var match = Arrays.asList(-target, nums[i], nums[map.get(target-nums[i])]);
                match.sort(null);
                result.add(match);
            } 
            map.put(nums[i], i);  
        }

        return result;
    }

    public List<List<Integer>> threeSum(int[] nums) {
        Set<List<Integer>> res = new HashSet<List<Integer>>();
        Arrays.sort(nums);
        for(int i=0;i<nums.length;i++){
            var sub = Arrays.stream(nums, i+1, nums.length).toArray();
            var resForOne = twoSum(sub, -nums[i]);
            res.addAll(resForOne);
        }
        return new ArrayList(res);
    }
}