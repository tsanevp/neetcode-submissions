class Solution:
    def climbStairs(self, n: int) -> int:
        if not n:
            return -1

        prev, curr = 0, 1
        for i in range(n):
            new = prev + curr
            prev = curr
            curr = new
        
        return curr
