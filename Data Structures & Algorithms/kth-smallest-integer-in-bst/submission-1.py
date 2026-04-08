# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        res = self.bst(res, root)

        return res[k - 1]
    
    def bst(self, res, root):
        if not root:
            return res
        
        self.bst(res, root.left)
        res.append(root.val)
        self.bst(res, root.right)

        return res

