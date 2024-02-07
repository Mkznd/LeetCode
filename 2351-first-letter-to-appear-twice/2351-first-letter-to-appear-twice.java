import java.util.HashSet;
class Solution {
    public char repeatedCharacter(String s) {
        var a = new HashSet<Character>();
        for(int i=0;i<s.length();i++){
            if(a.contains(s.charAt(i))){
                return s.charAt(i);
            }
            a.add(s.charAt(i));
        }
        return 's';
    }
    
}