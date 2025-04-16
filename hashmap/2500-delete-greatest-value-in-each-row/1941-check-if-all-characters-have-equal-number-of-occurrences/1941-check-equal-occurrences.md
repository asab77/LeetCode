# 1941. Check if All Characters Have Equal Number of Occurrences

🔗 [Link to Problem](https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences)

---

## 🧠 Problem Summary:
You're given a string `s`. You need to return `True` if **every character** in the string appears the **same number of times**, and `False` otherwise.

---

## ✅ Pattern(s) Used:
- **Pattern 1: Frequency Counting**
- **Pattern 2: All Values Must Be Equal**

---

## ❌ My First Confusion:
- I used `input_char` instead of the correct variable name `s`
- I didn’t know how to compare all the values in the frequency dictionary

---

## ✅ Final Approach:
1. Loop through each character in the string and count occurrences using a dictionary.
2. Extract all the values from the dictionary (the frequencies).
3. Compare each value to the first value to ensure all are equal.

---

## 💡 Key Trick:
```python
values = list(dic.values())
first_val = values[0]
for val in values:
    if val != first_val:
        return False
return True
```

---

## ⏱ Complexity:
- Time: O(n), where n is the length of the string
- Space: O(1), since the alphabet size is fixed and limited to lowercase English letters

---

## ✅ Code (Python):
```python
class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        dic = {}

        for char in s:
            if char in dic:
                dic[char] += 1
            else:
                dic[char] = 1

        values = list(dic.values())
        first_val = values[0]

        for val in values:
            if val != first_val:
                return False
        return True
```
