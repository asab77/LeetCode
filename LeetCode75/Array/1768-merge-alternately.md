# 1768. Merge Strings Alternately

🔗 [Link to Problem](https://leetcode.com/problems/merge-strings-alternately/?envType=study-plan-v2&envId=leetcode-75)

---

## 🧠 Problem Summary:
You're given two strings, `word1` and `word2`. You need to merge them by alternating characters from each string, starting with `word1`. If one string is longer, append the remaining characters to the end of the result.

---

## ❌ My First Thoughts:
I tried to loop over the total length of `word1 + word2`, assuming I could alternate characters using index math. I didn’t realize that using the total length could cause index out-of-range errors when the strings are different lengths. I was also confused about how to visualize `i < len(word1)` and why that check matters.

---

## ✅ Final Approach:
- First, find the max length of both strings using `max(len(word1), len(word2))`
- Loop from `0` to that max length
- At each index `i`, check if it exists in `word1` or `word2` before adding
- Append the characters safely using `if i < len(...)` checks

---

## 💡 Key Pattern:
- Alternating string merge
- Index-safe loop using `if i < len(...)` checks
- This is a **simulation** or **two-pointer** type problem with safe bounds checking

---

## ⏱ Complexity:
- Time: O(n), where n is the length of the longer string
- Space: O(n), for the output string

---

## ✅ Code (Python):
```python
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        max_len = max(len(word1), len(word2))
        for i in range(max_len):
            if i < len(word1):
                merged += word1[i]
            if i < len(word2):
                merged += word2[i]
        return merged
```

---

## ✅ Code (C++):
```cpp
class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string merged = "";
        int maxLen = max(word1.length(), word2.length());
        for (int i = 0; i < maxLen; ++i) {
            if (i < word1.length()) merged += word1[i];
            if (i < word2.length()) merged += word2[i];
        }
        return merged;
    }
};
```
