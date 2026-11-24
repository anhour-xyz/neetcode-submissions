class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        for i in range(len(flowerbed)):
            if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] != 1:
                n -= 1
            elif i == len(flowerbed) - 1 and flowerbed[i] == 0 and flowerbed[i-1] != 1:
                n -= 1
            elif i >= 1 and i < len(flowerbed) -1:
                if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                    n -= 1
        return n <= 0
