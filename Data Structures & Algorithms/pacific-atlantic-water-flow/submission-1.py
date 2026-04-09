class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []

        if not heights:
            return res
        
        # down, up, right, left
        flowDir = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pacific, atlantic = set(), set()
        pq, aq = [], []

        m, n = len(heights), len(heights[0])

        for row in range(m):
            for col in range(n):
                if row == 0 or col == 0:
                    pq.append((row, col))
                
                if row == m - 1 or col == n - 1:
                    aq.append((row, col))
        
        for curr in pq:
            q = deque()
            q.append(curr)

            while q:
                row, col = q.popleft()

                if (row, col) in pacific:
                    continue
                
                pacific.add((row, col))
                temp = heights[row][col]

                for dr, dc in flowDir:
                    nr, nc = row + dr, col + dc
                    if nr >= 0 and nr < m and nc >= 0 and nc < n and heights[nr][nc] >= temp and (nr, nc) not in pacific:
                        q.append((nr, nc))
                    
        for curr in aq:
            q = deque()
            q.append(curr)

            while q:
                row, col = q.popleft()

                if (row, col) in atlantic:
                    continue
            
                atlantic.add((row, col))
                temp = heights[row][col]

                for dr, dc in flowDir:
                    nr, nc = row + dr, col + dc
                    if nr >= 0 and nr < m and nc >= 0 and nc < n and heights[nr][nc] >= temp and (nr, nc) not in atlantic:
                        q.append((nr, nc))

        return list(pacific & atlantic)
        

