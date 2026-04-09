class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        
        pq, aq = [], []
        m, n = len(heights), len(heights[0])

        # down, up, right, left
        flowDir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    pq.append((row, col))
                
                if row == m - 1 or col == n - 1:
                    aq.append((row, col))
        
        pacific = self.bfs(heights, pq, m, n, flowDir)
        atlantic = self.bfs(heights, aq, m, n, flowDir)

        return list(pacific & atlantic)
        

    def bfs(self, heights, source, m, n, flowDir):
        ocean = set()
        
        for curr in source:
            q = deque()
            q.append(curr)

            while q:
                row, col = q.popleft()

                if (row, col) in ocean:
                    continue
            
                ocean.add((row, col))
                temp = heights[row][col]

                for dr, dc in flowDir:
                    nr, nc = row + dr, col + dc
                    if nr >= 0 and nr < m and nc >= 0 and nc < n and heights[nr][nc] >= temp and (nr, nc) not in ocean:
                        q.append((nr, nc))
        
        return ocean

