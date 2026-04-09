class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()
        def dfs(node, par):
            if node in visit:
                return False
            
            visit.add(node)
            for neigh in adj[node]:
                if neigh == par:
                    continue
                
                if not dfs(neigh, node):
                    return False

            return True                

        return dfs(0, None) and len(visit) == n