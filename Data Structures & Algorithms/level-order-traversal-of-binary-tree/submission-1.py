# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root:
            return res
        
        q = deque()
        q.append(root)

        while q:
            row = []
            for _ in range(len(q)):
                temp = q.popleft()
                row.append(temp.val)
                
                if temp.left:
                    q.append(temp.left)
                
                if temp.right:
                    q.append(temp.right)
            
            res.append(row)
        
        return res
                