class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0,0
        p = []
        for i in path:
            p.append((x,y))
            if i=="N":
                y+=1
            elif i=="S":
                y-=1
            elif i=="E":
                x+=1
            else:
                x-=1
            if (x,y) in p:
                return True
            
        return False
        