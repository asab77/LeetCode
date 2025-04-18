class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        candy_len = len(candies)
        result = []

        for i in range(candy_len):
            if (candies[i] + extraCandies >= max_candy):
                result.append(True)
            else:
                result.append(False)

        return result
        
