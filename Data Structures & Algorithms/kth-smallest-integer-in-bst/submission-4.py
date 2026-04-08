# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            
            root = root.right
        
        return -1

