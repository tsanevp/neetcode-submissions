class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        
        if not strs:
            return encoded
                
        for val in strs:
            encoded += f"{len(val)}%{val}"
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []

        if not s:
            return decoded
        
        left = right = 0
        while left < len(s):
            if s[right] == '%':
                length = int(s[left:right])
                right += 1
                left = right + length

                decoded.append(s[right:left])
                right = left
            else:
                right += 1
        
        return decoded