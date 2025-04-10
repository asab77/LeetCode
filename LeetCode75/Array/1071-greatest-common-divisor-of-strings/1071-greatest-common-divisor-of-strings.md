# 1071. Greatest Common Divisor of Strings

🔗 [Link to Problem](https://leetcode.com/problems/greatest-common-divisor-of-strings)

---

## 🧠 Problem Summary:
Given two strings `str1` and `str2`, return the largest string `x` such that `x` divides both `str1` and `str2`. A string `x` divides `s` if `s` is made by concatenating `x` one or more times.

---

## ❌ My First Thoughts:
I thought I needed to remove repeated appearances of one string from the other and store them in a result string, like "subtracting" repeated substrings. But I realized this approach wouldn't help me identify the actual repeating base that could divide both strings.

---

## ✅ Final Approach:
- If `str1 + str2 != str2 + str1`, then they don't share a common repeating base, and the answer is `""`.
- If they do match, then the true base must be a substring of length equal to the GCD of `len(str1)` and `len(str2)`.
- Extract the substring of length `gcd(len(str1), len(str2))` from either string and return it.

---

## 💡 Key Pattern:
- String simulation
- GCD of string lengths
- If `str1 + str2 == str2 + str1`, they have the same repeating pattern

---

## ⏱ Complexity:
- Time: O(n), where n is the combined length of both strings
- Space: O(1), ignoring output string

---

## ✅ Code (Python):
```python
from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        gcd_len = gcd(len(str1), len(str2))
        return str1[:gcd_len]
```

---

## ✅ Code (C++):
```cpp
class Solution {
public:
    string gcdOfStrings(string str1, string str2) {
        if (str1 + str2 != str2 + str1) return "";
        int gcdLen = gcd(str1.length(), str2.length());
        return str1.substr(0, gcdLen);
    }
};
```
