class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> a = new HashMap<>();
        for (String s: strs){
            var chars = s.toCharArray();
            Arrays.sort(chars);
            var key = new String(chars);
            a.computeIfAbsent(key, k -> new ArrayList<String>()).add(s);
        }
        List<List<String>> res = new ArrayList<>();
        for(var i: a.values()){
            res.add(i);
        }
        return res;
    }
}