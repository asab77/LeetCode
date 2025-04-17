class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        dic = {}

        for u,v in edges:
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

        
