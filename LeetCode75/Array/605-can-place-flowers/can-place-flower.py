class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        length = len(flowerbed)
        
        while i < length:
            # If current plot is empty AND both neighbors (if they exist) are empty
            if (flowerbed[i] == 0 and
                (i == 0 or flowerbed[i - 1] == 0) and
                (i == length - 1 or flowerbed[i + 1] == 0)):
                
                flowerbed[i] = 1  # plant flower
                n -= 1            # one less flower to plant
                i += 2            # skip next plot
            else:
                i += 1            # move to next plot

        return n <= 0
