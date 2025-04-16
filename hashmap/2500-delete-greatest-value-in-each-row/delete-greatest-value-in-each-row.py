class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        count = 0
        while grid[0]:  # while there's still at least one column
            max_values = []

            for row in grid:
                max_val = max(row)            # find the max value in the row
                row.remove(max_val)           # remove it from the row
                max_values.append(max_val)    # save it

            count += max(max_values)          # add the biggest of all to the count
        
        return count



        
