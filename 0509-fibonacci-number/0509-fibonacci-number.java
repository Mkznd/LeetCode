class Solution {
    public int fib(int n) {
        if(n<2){
            return n;
        }
        
        int pre=0, cur=1;
        for(int i=2;i<=n;i++){
            var t = pre;
            pre = cur;
            cur = t+cur;
        }
        return cur;
    }
}