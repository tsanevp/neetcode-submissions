class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        stack = []
        mapping = {'(': ')', '{': '}', '[': ']'}

        for val in s:
            if val in mapping:
                stack.append(val)
                continue
            
            if not stack:
                return False
            
            top = stack.pop(-1)
            if mapping[top] != val:
                return False
            
        return not stack
