class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        if not s:
            return res
        
        n = len(s)
        for i in range(n):
            left = right = i

            while right + 1 < n and s[i] == s[right + 1]:
                right += 1
                res += 1
            
            while left - 1 >= 0 and right + 1 < n and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
                res += 1
            
            res += 1
        
        return res
