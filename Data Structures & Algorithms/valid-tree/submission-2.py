class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False
        
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visit = set()

        q = deque()
        q.append((0, None))
        while q:
            node, par = q.popleft()
            if node in visit:
                return False
            
            visit.add(node)
            for neigh in adj[node]:
                if neigh == par:
                    continue
                q.append((neigh, node))                

        return len(visit) == n