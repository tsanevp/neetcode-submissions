class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        n, m = len(board), len(board[0])
        for row in range(n):
            for col in range(m):
                if board[row][col] == word[0]:
                    if self.dfs(board, row, col, word, 1):
                        return True
                    
        return False

    def dfs(self, board, row, col, word, length):
        n, m = len(board), len(board[0])

        temp = board[row][col]
        board[row][col] = '#'
        if length == len(word):
            return True

        left = right = up = down = False
        if col - 1 >= 0 and board[row][col - 1] == word[length]:
            left = self.dfs(board, row, col - 1, word, length + 1)
        if col + 1 < m and board[row][col + 1] == word[length]:
            right = self.dfs(board, row, col + 1, word, length + 1)
        if row - 1 >= 0 and board[row - 1][col] == word[length]:
            up = self.dfs(board, row - 1, col, word, length + 1)
        if row + 1 < n and board[row + 1][col] == word[length]:
            down = self.dfs(board, row + 1, col, word, length + 1)
        
        board[row][col] = temp
        return left or right or up or down