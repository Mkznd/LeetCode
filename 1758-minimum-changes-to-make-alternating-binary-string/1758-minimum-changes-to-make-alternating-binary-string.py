class Solution:
    def minOperations(self, s: str) -> int:
        a = "".join([str(i%2) for i in range(len(s))])
        b = "".join([str(int(not i%2)) for i in range(len(s))])
        res = min(
            len([i for i in range(len(a)) if a[i]!=s[i]]),
            len([i for i in range(len(b)) if b[i]!=s[i]]),
        )
        return res