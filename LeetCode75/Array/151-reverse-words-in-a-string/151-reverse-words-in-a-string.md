# 151. Reverse Words in a String

🔗 [Link to Problem](https://leetcode.com/problems/reverse-words-in-a-string)

---

## 🧠 Problem Summary:
Given an input string `s`, reverse the order of the words.  
A word is defined as a sequence of non-space characters. Words are separated by spaces, but there may be leading/trailing spaces or multiple spaces between words.  
Return a string of the words in reverse order, joined by a **single space**, and with no extra spaces.

---

## ❌ My First Thoughts:
- I wanted to do everything manually: trim spaces, clean multiple spaces, reverse the characters, then join them back.
- I hit issues with "index out of range" errors and string immutability in Python.
- It became hard to manage and debug even though the idea was working conceptually.

---

## ✅ Final Approach:
- Use `s.split()` to split the string into words automatically (handles all whitespace properly).
- Use `.reverse()` or slicing to reverse the word list.
- Use `' '.join(...)` to combine the words into the final result with exactly one space between them.

---

## 💡 Key Pattern:
- Built-in string processing with `split()` and `join()`
- Handles all edge cases (extra spaces, leading/trailing/multiple spaces)

---

## ⏱ Complexity:
- Time: O(n), where n is the length of the input string
- Space: O(n), for the words list

---

## ✅ Code (Python):
```python
class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()        # handles all extra spaces automatically
        words.reverse()          # reverse the list in-place
        return ' '.join(words)   # return joined string with single spaces
```
