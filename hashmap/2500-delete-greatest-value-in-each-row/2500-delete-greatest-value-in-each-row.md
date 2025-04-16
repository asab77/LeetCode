# 2500. Delete Greatest Value in Each Row

🔗 [Link to Problem](https://leetcode.com/problems/delete-greatest-value-in-each-row)

---

## 🧠 Problem Summary:
You're given an `m x n` matrix `grid`. In each round, remove the greatest value from **each row**, and:
- Among all those removed values, take the **maximum one**
- Add that max to your result

Repeat this process until the grid is empty.

---

## ✅ Pattern(s) Used:
- **2D Array Traversal**
- **Dynamic Row Updates**
- (Optional) **List Sorting** or **Manual max-removal**

---

## ❌ My Initial Struggles:
- I was confused whether to create a dummy grid
- I tried removing elements directly from the matrix incorrectly (`dum_list.remove(max_val)`)
- I thought I had to sort everything — but found out I could avoid that

---

## ✅ Final Approach (Without Sorting):
1. Loop while the grid still has columns.
2. For each row:
   - Get the maximum value
   - Remove it from the row
   - Add it to a temporary list
3. After each round, get the maximum from the temporary list and add it to the total.

---

## 💡 Key Insight:
Instead of sorting, we can use:
```python
max_val = max(row)
row.remove(max_val)
```
This avoids the overhead of sorting and is easier to understand.

---

## ⏱ Complexity:
- Time: O(m * n²) in worst case if removing max takes O(n) per row
- Space: O(m) for holding the list of deleted values per iteration

---

## ✅ Code (Python):
```python
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        count = 0

        while grid[0]:
            max_values = []

            for row in grid:
                max_val = max(row)
                row.remove(max_val)
                max_values.append(max_val)

            count += max(max_values)

        return count
```
