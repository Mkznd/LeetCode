class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        prev = False
        for i in range(len(flowerbed)-1):
            if not prev and not flowerbed[i+1] and not flowerbed[i]:
                flowerbed[i]=1
                n-=1

            prev = flowerbed[i]
        n-= (not flowerbed[-1] and not prev)
        return n <= 0