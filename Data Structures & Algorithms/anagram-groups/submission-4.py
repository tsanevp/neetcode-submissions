class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return False
        
        groups = {}
        for word in strs:
            count = self.getCount(word)

            if count in groups:
                groups[count].append(word)
            else:
                groups[count] = [word]
        
        return list(groups.values())
    
    def getCount(self, word):
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        
        return tuple(count)
