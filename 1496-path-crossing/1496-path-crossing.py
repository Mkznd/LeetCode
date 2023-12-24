class Solution:
    def isPathCrossing(self, path: str) -> bool:
        a = {"N": 1, "S": -1, "E": 0, "W": 0}
        b = {"E": 1, "W": -1,"N": 0, "S": 0 }

        x, y = 0,0
        p = set()
        for i in path:
            p.add((x,y))
            y+=a[i]
            x+=b[i]
            if (x,y) in p:
                return True   
        return False
        