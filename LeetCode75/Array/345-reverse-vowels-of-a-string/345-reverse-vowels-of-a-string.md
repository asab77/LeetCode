# 345. Reverse Vowels of a String

🔗 [Link to Problem](https://leetcode.com/problems/reverse-vowels-of-a-string)

---

## 🧠 Problem Summary:
Given a string `s`, reverse only the vowels in the string and return the resulting string.  
Vowels include both lowercase and uppercase: `a, e, i, o, u` and `A, E, I, O, U`.

---

## ❌ My First Thoughts:
- I knew I needed to identify all the vowels in the string.
- I started by appending vowels to a list and wanted to then replace the original vowels with the reversed ones.
- I mistakenly used `str` as a variable name, and I tried modifying the string directly using indexing, which isn't allowed in Python because strings are immutable.

---

## ✅ Final Approach:
- Convert the string into a list so I can modify characters.
- Collect all the vowels into a list while preserving their order.
- Loop through the string again, and for each vowel, replace it with the **last vowel from the list** using `pop()`.
- Join the modified list back into a string at the end.

---

## 💡 Key Pattern:
- Two-pass string traversal
- Vowel detection using `char.lower() in 'aeiou'`
- Rebuilding string via list conversion

---

## ⏱ Complexity:
- Time: O(n), where n is the length of the string
- Space: O(k), where k is the number of vowels

---

## ✅ Code (Python):
```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        s = list(s)

        for char in s:
            if char.lower() in 'aeiou':
                vowels.append(char)

        for i in range(len(s)):
            if s[i].lower() in 'aeiou':
                s[i] = vowels.pop()

        return ''.join(s)
```
