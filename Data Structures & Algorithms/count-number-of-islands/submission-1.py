class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        if not grid:
            return res

        ones = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    ones.add((row, col))
        
        while ones:
            res += 1
            curr = ones.pop()

            q = deque()
            q.append(curr)
            while q:
                row, col = q.popleft()
                # left
                if col - 1 >= 0 and grid[row][col - 1] == "1":
                    if (row, col - 1) in ones:
                        ones.remove((row, col - 1))
                        q.append((row, col - 1))
                # right
                if col + 1 < len(grid[0]) and grid[row][col + 1] == "1":
                    if (row, col + 1) in ones:
                        ones.remove((row, col + 1))
                        q.append((row, col + 1))
                # up
                if row - 1 >= 0 and grid[row - 1][col] == "1":
                    if (row - 1, col) in ones:
                        ones.remove((row - 1, col))
                        q.append((row - 1, col))
                # down
                if row + 1 < len(grid) and grid[row + 1][col] == "1":
                    if (row + 1, col) in ones:
                        ones.remove((row + 1, col))
                        q.append((row + 1, col))
        
        return res