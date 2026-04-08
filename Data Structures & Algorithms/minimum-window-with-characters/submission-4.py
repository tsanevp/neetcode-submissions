class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # get count of each char
        # get num of matches needed
        # create curr count in str

        # have two pointers, right and left

        # iter right and increase the current count
        # each time we iter the current count, compare to parent count
        # if equal, increment matches
            # if matches == len(parentcount),
                # get length curr substring
                #then move left pointer until we reach another value in t
        if len(t) > len(s):
            return ""
        
        countT, countS = {}, {}
        for val in t:
            countT[val] = countT.get(val, 0) + 1
        
        res = []
        neededMatches, matches = len(countT), 0
        left = 0

        for right in range(len(s)):
            char = s[right]
            if char not in countT:
                continue
            
            countS[char] = countS.get(char, 0) + 1
            if countS[char] < countT[char] or countS[char] > countT[char]:
                continue

            # matched case b/c we will never have more than countT
            matches += 1
            while left <= right and neededMatches == matches:
                currLen = (right - left) + 1
                if not res or currLen < (res[1] - res[0] + 1):
                    res = [left, right]
                
                curr = s[left]
                if curr in countT:
                    countS[curr] -= 1

                    if countS[curr] < countT[curr]:
                        matches -= 1

                left += 1
        return s[res[0]:res[1] + 1] if res else ""

