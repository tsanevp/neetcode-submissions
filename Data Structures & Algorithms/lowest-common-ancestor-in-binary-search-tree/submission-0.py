class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        
        pIsRoot = root if root.val == p.val else None
        qIsRoot = root if root.val == q.val else None

        if left and pIsRoot:
            return pIsRoot
        
        if left and qIsRoot:
            return qIsRoot
        
        if right and pIsRoot:
            return pIsRoot
        
        if right and qIsRoot:
            return qIsRoot
        
        return (left or right or pIsRoot or qIsRoot)