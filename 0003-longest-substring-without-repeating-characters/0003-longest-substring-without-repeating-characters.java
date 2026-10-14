class Solution {
    public int lengthOfLongestSubstring(String s) {
        int l=0, r=0;
        int maxL = 0;
        Set<Character> cur = new HashSet<>();
        int currentLength = 0;

        while(r<s.length()){
            while(r < s.length() && !cur.contains(s.charAt(r))){
                cur.add(s.charAt(r++));
                currentLength++;
            }
            maxL = Math.max(maxL, currentLength);
            cur.remove(s.charAt(l++));
            currentLength -= 1;
        }

        return maxL;
    }
}