class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        a = {i[0]:i[1] for i in paths}
        n = paths[0][0]
        x = a[n]
        while a.get(x):
            x = a[x]
        return x
        