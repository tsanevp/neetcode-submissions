class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[-1] = True

        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if (i + len(word) <= len(s)) and s[i:i+len(word)] == word:
                    dp[i] = dp[i+len(word)] if dp[i] == False else dp[i]
                    
        return dp[0]


        
        # "n  e  e  t  c  o  d  e"
        # [F, F, F, F, F, F, F, F, T]
        #  0  1  2  3  4  5  6  7  8

        # "a  b  c  d"
        # [T, T, T, F, T]
        #  0  1  2  3