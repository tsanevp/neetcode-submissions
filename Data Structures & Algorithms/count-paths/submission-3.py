class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev = [0] * n

        for row in range(m - 1, -1, -1):
            curr = [0] * n
            curr[-1] = 1

            for col in range(n - 2, -1, -1):
                curr[col] += prev[col] + curr[col + 1]
            
            prev = curr
        
        return prev[0]

       

