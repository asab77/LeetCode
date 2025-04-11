# 605. Can Place Flowers

🔗 [Link to Problem](https://leetcode.com/problems/can-place-flowers)

---

## 🧠 Problem Summary:
You're given a flowerbed represented as an array of `0`s (empty) and `1`s (planted). You need to determine if it's possible to plant `n` new flowers in the empty plots without violating the rule that **no two flowers can be planted in adjacent plots**.

---

## ❌ My First Thoughts:
- At first, I thought maybe I could just count zeros and use that to decide how many flowers to plant.
- But I realized it's not enough to count — I need to **check neighbors** to make sure there's no violation of the no-adjacent rule.
- I was also confused if flowers could be added at the end of the flowerbed, but understood later that I must use only the given array and can’t add extra space.

---

## ✅ Final Approach:
- Loop through the array.
- If the current plot is `0`, and both the left and right plots (if they exist) are `0` or out of bounds, we can plant a flower here.
- Mark it as planted (`1`) and skip the next index since flowers can't be adjacent.
- Decrement `n` each time a flower is planted.
- Return `True` if we planted all `n` flowers, otherwise `False`.

---

## 💡 Key Pattern:
- Simulation + Greedy
- In-place update of the array
- Check bounds safely for edge plots

---

## ⏱ Complexity:
- Time: O(n), where n is the length of the flowerbed
- Space: O(1), since we're modifying the input array

---

## ✅ Code (Python):
```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        length = len(flowerbed)
        
        while i < length:
            if (flowerbed[i] == 0 and
                (i == 0 or flowerbed[i - 1] == 0) and
                (i == length - 1 or flowerbed[i + 1] == 0)):
                
                flowerbed[i] = 1
                n -= 1
                i += 2
            else:
                i += 1

        return n <= 0
```

---

## ✅ Code (C++):
```cpp
class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        int i = 0;
        int length = flowerbed.size();

        while (i < length) {
            if (flowerbed[i] == 0 &&
                (i == 0 || flowerbed[i - 1] == 0) &&
                (i == length - 1 || flowerbed[i + 1] == 0)) {
                
                flowerbed[i] = 1;
                n--;
                i += 2;
            } else {
                i++;
            }
        }

        return n <= 0;
    }
};
```
