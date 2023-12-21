class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        a = {} # sorted() : index in res
        res = []
        ind = 0
        for i in strs:
            temp = str(sorted(i))
            if temp in a.keys():
                res[a[temp]].append(i)
            else:
                a[temp] = len(res)
                res.append([i])
        return res