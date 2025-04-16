class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        count = 0

        for row in range(len(grid)):
            for col in range(len(grid)):

                row_list = grid[row]
                col_list = [grid[r][col] for r in range(len(grid))]

                if row_list == col_list: count += 1

        return count
