# 1971. Find if Path Exists in Graph

🔗 [Link to Problem](https://leetcode.com/problems/find-if-path-exists-in-a-graph)

---

## 🧠 Problem Summary:
You're given:
- An integer `n` representing the number of nodes (0 to n - 1)
- A list of undirected edges connecting pairs of nodes
- Two integers: `source` and `destination`

Return `True` if there is a path from `source` to `destination`. Otherwise, return `False`.

---

## ✅ Pattern(s) Used:
- Graph Construction (Adjacency List)
- DFS (Depth-First Search)
- Visited Set

---

## ❌ My Initial Confusion:
- Wasn't sure how to build the graph from edge pairs
- Didn't understand `.get(node, [])` and why it's safer than `dic[node]`

---

## ✅ Final Approach:
1. Create an adjacency list from edges (undirected graph).
2. Use DFS to explore from `source` node.
3. Track visited nodes in a `set()` to prevent infinite recursion.
4. Return `True` as soon as `destination` is reached.
5. Return `False` if no path exists after all options are explored.

---

## 💡 Key Insight:
Use `.get(node, [])` instead of `dic[node]` to safely handle nodes that may have no neighbors:
```python
for neighbor in dic.get(node, []):
```
This avoids potential `KeyError` if a node isn't in the dictionary.

---

## ⏱ Complexity:
- Time: O(N + E), where N = number of nodes, E = number of edges
- Space: O(N) for the visited set and recursion stack

---

## ✅ Final Code (Python):
```python
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Build the graph
        dic = {}
        for u, v in edges:
            dic.setdefault(u, []).append(v)
            dic.setdefault(v, []).append(u)

        visited = set()

        def dfs(node):
            if node == destination:
                return True
            visited.add(node)
            for neighbor in dic.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False

        return dfs(source)
```
