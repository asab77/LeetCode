# 2006. Count Number of Pairs With Absolute Difference K

🔗 [Link to Problem](https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k)

---

## 🧠 Problem Summary:
You're given an array of integers `nums` and an integer `k`.  
You need to count how many **pairs `(i, j)`** exist such that:
- `i < j`
- `|nums[i] - nums[j]| == k`

---

## ✅ Pattern(s) Used:
- **Nested Loop with Condition Check**
- **Absolute Difference Comparison**

---

## ❌ My First Mistake:
- I used `for j in range(1, len(nums))`, which caused some comparisons where `j <= i`.
- This violated the rule `i < j` and gave incorrect results.

---

## ✅ Final Approach:
1. Use a nested loop.
2. Start the inner loop from `i + 1` to ensure `i < j`.
3. Check `abs(nums[i] - nums[j]) == k`
4. If true, increment the count.

---

## 💡 Key Insight:
To follow the condition `i < j`, always start `j` from `i + 1`:
```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
```

---

## ⏱ Complexity:
- Time: O(n²), where n is the length of `nums` (nested loops)
- Space: O(1)

---

## ✅ Code (Python):
```python
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) == k:
                    count += 1

        return count
```
