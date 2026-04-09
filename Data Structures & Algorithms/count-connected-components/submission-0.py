class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not edges:
            return n
        
        adj = [[] for i in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        visited = set()
        islands = 0
        for i in range(n):
            if i in visited:
                continue
            
            islands += 1
            q = deque()
            q.append((i, None))
            while q:
                node, par = q.popleft()
                if node in visited:
                    continue
                
                visited.add(node)
                for neigh in adj[node]:
                    if neigh == par:
                        continue

                    q.append((neigh, node))
        
        return islands
            