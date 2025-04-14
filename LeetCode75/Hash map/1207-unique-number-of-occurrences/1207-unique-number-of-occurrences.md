# 1207. Unique Number of Occurrences

🔗 [Link to Problem](https://leetcode.com/problems/unique-number-of-occurrences)

---

## 🧠 Problem Summary:
You're given an array of integers. Return `True` if the number of times each value appears is unique.  
In other words, **no two different numbers** should have the **same frequency**.

---

## ✅ Pattern(s) Used:
- **Pattern 1: Frequency Counting** — Count how many times each value appears using a dictionary.
- **Pattern 2: Check for Duplicates** — Use a set to detect if any frequencies are repeated.

---

## ❌ My First Thought:
- I wanted to use a dictionary to track how many times each number appears.
- At first I tried looping directly and assigning `dic[arr]`, but I forgot to update the frequency or handle duplicates.
- I also used `for arr in arr`, which caused a naming conflict.

---

## ✅ Final Approach:
1. Use a dictionary to count how many times each number appears.
2. Extract the dictionary's values (the frequencies).
3. Convert the values to a set and compare lengths:
   - If the set is smaller than the list, it means some values were duplicated.

---

## 💡 Key Trick:
```python
len(freqs) == len(set(freqs))
```
If this is `True`, all frequencies are unique.

---

## ⏱ Complexity:
- Time: O(n), where n is the length of the input array
- Space: O(n), for the dictionary and set

---

## ✅ Code (Python):
```python
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = {}

        for num in arr:
            dic[num] = dic.get(num, 0) + 1

        freqs = list(dic.values())
        return len(freqs) == len(set(freqs))
```
