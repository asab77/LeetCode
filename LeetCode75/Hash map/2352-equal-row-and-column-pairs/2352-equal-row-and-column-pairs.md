# 2352. Equal Row and Column Pairs

🔗 [Link to Problem](https://leetcode.com/problems/equal-row-and-column-pairs)

---

## 🧠 Problem Summary:
You're given an `n x n` grid (2D list). You need to count how many pairs `(row i, column j)` exist such that row `i` and column `j` are exactly the same — same elements in the same order.

---

## ✅ Pattern(s) Used:
- **Compare Row and Column Directly**  
  Convert a column to a list using list comprehension and compare it directly with a row.

---

## ❌ My First Confusion:
- I didn't know how to extract a **column** from a 2D list.
- I thought you could just do `grid[col]`, but that gives another row, not a column.
- It wasn’t clear how to get a vertical slice of the grid.

---

## 💡 Key Trick:
To extract a full column as a list, use:
```python
col_list = [grid[r][col] for r in range(len(grid))]
```

This means:
- Loop over all rows `r`
- At each row, grab the `col`-th element
- The result is a list of values from top to bottom in that column

---

## ✅ Final Approach:
1. Loop through each row index `i` and each column index `j`
2. Grab the full row as `row_list = grid[i]`
3. Build the full column as a list using list comprehension
4. Compare the two lists
5. If equal, increment the counter

---

## ⏱ Complexity:
- Time: O(n³) because for each row and column pair, you build a column list (O(n)) and compare lists (O(n))
- Space: O(n) for the temporary column list

---

## ✅ Code (Python):
```python
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0

        for row in range(len(grid)):
            for col in range(len(grid)):
                row_list = grid[row]
                col_list = [grid[r][col] for r in range(len(grid))]

                if row_list == col_list:
                    count += 1

        return count
```
