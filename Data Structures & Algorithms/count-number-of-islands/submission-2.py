class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        if not grid:
            return res

        n, m = len(grid), len(grid[0])
        visited = [([False] * m) for _ in range(n)]

        for row in range(n):
            for col in range(m):
                if grid[row][col] == "1" and not visited[row][col]:
                    res += 1
                    visited = self.bfs(row, col, grid, visited)
        
        return res

    def bfs(self, row, col, grid, visited):
        q = deque()
        q.append((row, col))
        
        while q:
            row, col = q.popleft()
            if visited[row][col]:
                continue

            visited[row][col] = True

            # left
            if col - 1 >= 0 and grid[row][col - 1] == "1":
                q.append((row, col - 1))
            # right
            if col + 1 < len(grid[0]) and grid[row][col + 1] == "1":
                q.append((row, col + 1))
            # up
            if row - 1 >= 0 and grid[row - 1][col] == "1":
                q.append((row - 1, col))
            # down
            if row + 1 < len(grid) and grid[row + 1][col] == "1":
                q.append((row + 1, col))
        
        return visited