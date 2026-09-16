class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = [0] * 26
        for ch in s:
            countS[ord(ch) - ord('a')] += 1
        
        for ch in t:
            countS[ord(ch) - ord('a')] -= 1
        
        for i in range(len(countS)):
            if countS[i] != 0:
                return False
        
        return True