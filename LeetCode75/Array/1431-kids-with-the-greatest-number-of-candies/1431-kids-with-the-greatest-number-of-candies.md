# 1431. Kids With the Greatest Number of Candies

🔗 [Link to Problem](https://leetcode.com/problems/kids-with-the-greatest-number-of-candies)

---

## 🧠 Problem Summary:
You're given an array `candies`, where `candies[i]` is the number of candies the i-th kid has, and a number `extraCandies` you can give to one kid at a time.  
Return a boolean list where each element is True if that kid, after receiving all `extraCandies`, could have the most candies among all kids.

---

## ❌ My First Thoughts:
- I correctly found the max number of candies using `max(candies)`
- But I made mistakes like:
  - Typing `can_len` instead of `candy_len`
  - Using `result[i].add(...)` which caused an index error (since the result list was initially empty)
  - The condition `max_candy > candies[i]` was backward logic

---

## ✅ Final Approach:
- First, get the current max number of candies
- Loop over each kid
- For each kid, check if their candies + `extraCandies` is at least the current max
- Append `True` or `False` to the result list accordingly

---

## 💡 Key Pattern:
- Array traversal
- Simple simulation with a comparison check
- Basic use of `append()` and comparison logic

---

## ⏱ Complexity:
- Time: O(n), where n is the number of kids
- Space: O(n), for the result list

---

## ✅ Code (Python):
```python
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        result = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max_candy:
                result.append(True)
            else:
                result.append(False)
        return result
```

---

## ✅ Code (C++):
```cpp

#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<bool> kidsWithCandies(std::vector<int>& candies, int extraCandies) {
        int maxCandy = *std::max_element(candies.begin(), candies.end());
        std::vector<bool> result;

        for (int i = 0; i < candies.size(); ++i) {
            result.push_back(candies[i] + extraCandies >= maxCandy);
        }

        return result;
    }
};
```
