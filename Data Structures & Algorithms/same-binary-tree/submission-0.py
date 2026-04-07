# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if not p or not q:
            return False
        
        qu = [(p, q)]
        while qu:
            pcurr, qcurr = qu.pop(0)
            
            if not pcurr and not qcurr:
                continue
            
            if not pcurr or not qcurr:
                return False

            if pcurr.val != qcurr.val:
                return False
            
            qu.append((pcurr.left, qcurr.left))
            qu.append((pcurr.right, qcurr.right))
        
        return True