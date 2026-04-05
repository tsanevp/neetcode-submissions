class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0

        if not s:
            return res
        
        left, seen = 0, {}
        for right, val in enumerate(s):
            if val in seen:
                left = max(left, seen[val] + 1)
            
            seen[val] = right
            res = max(res, right - left + 1)
        
        return res