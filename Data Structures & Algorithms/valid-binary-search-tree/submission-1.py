# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        q = deque()
        q.append((root, -1001, 1001))

        while q:
            for _ in range(len(q)):
                root, left, right = q.popleft()

                if root.val >= right or root.val <= left:
                    return False

                if root.left:
                    if root.left.val >= root.val or root.left.val >= right:
                        return False
                    
                    q.append((root.left, left, root.val))
                
                if root.right:
                    if root.right.val <= root.val or root.right.val <= left:
                        return False
                    
                    q.append((root.right, root.val, right))
        
        return True