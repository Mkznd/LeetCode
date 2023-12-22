class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        res = []
        for i in words:
            res.extend(i.split(separator))
        return [i for i in res if i]