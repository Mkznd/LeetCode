class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = {}
        for index, i in enumerate(s):
            if a.get(i) == None:
                a[i] = index
            else:
                a[i] = -1
        if all(i == -1 for i in a.values()):
            return -1
        return sorted(i for i in a.values() if i != -1)[0]