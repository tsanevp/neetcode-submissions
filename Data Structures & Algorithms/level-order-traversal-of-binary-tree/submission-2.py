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
                if not temp:
                    continue

                row.append(temp.val)
                q.append(temp.left)
                q.append(temp.right)
            
            if row:
                res.append(row)
        
        return res
                