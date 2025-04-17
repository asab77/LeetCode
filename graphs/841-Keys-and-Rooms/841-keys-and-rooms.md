# 841. Keys and Rooms

🔗 [Link to Problem](https://leetcode.com/problems/keys-and-rooms)

---

## 🧠 Problem Summary:
You are given a list of rooms, each containing keys to other rooms. You start in room 0.  
Return `True` if you can visit **all** rooms, otherwise return `False`.

---

## ✅ Pattern(s) Used:
- Graph Traversal
- DFS (Depth-First Search)
- Set for visited tracking

---

## ❌ My First Confusion:
- I wasn’t sure how to model rooms as a graph.
- I didn’t know if I needed a visited tracker (yes, you do).
- I tried `if key == visited` instead of checking membership in a set.

---

## ✅ Final Approach:
1. Treat each room as a node.
2. Keys inside rooms are edges to other nodes.
3. Use DFS to explore from room 0.
4. Track visited rooms using a set.
5. At the end, if the number of visited rooms equals total rooms, return True.

---

## 💡 Key Insight:
Use a set for visited rooms and recursive DFS to visit all reachable rooms.

```python
visited = set()

def dfs(room):
    visited.add(room)
    for key in rooms[room]:
        if key not in visited:
            dfs(key)
```

Start DFS with:
```python
dfs(0)
```

And finish with:
```python
return len(visited) == len(rooms)
```

This is cleaner than:
```python
if len(visited) == len(rooms):
    return True
else:
    return False
```

Both work — one is just shorter and more idiomatic in Python.

---

## ⏱ Complexity:
- Time: O(N + E), where N is the number of rooms, E is the number of keys (edges)
- Space: O(N) for the visited set and recursion stack

---

## ✅ Final Code:
```python
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(room):
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)

        dfs(0)
        return len(visited) == len(rooms)
```
