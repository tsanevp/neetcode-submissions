class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = right = 0
        res = []
        n = len(s)
        for i in range(n):
            left = right = i
            while right + 1 < n and s[i] == s[right + 1]:
                right += 1

            while left - 1 >= 0 and right + 1 < n and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1

            if not res or (right - left + 1) > (res[1] - res[0]):
                res = [left, right + 1]
        
        return s[res[0]:res[1]]
