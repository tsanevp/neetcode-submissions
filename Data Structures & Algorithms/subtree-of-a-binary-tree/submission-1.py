# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        
        if root and not subRoot:
            return True
        
        if not root and subRoot:
            return False

        que = deque()
        que.append(root)
        while que:
            node = que.popleft()

            if not node:
                continue
            
            if node.val == subRoot.val:
                if self.isSameTree(node, subRoot):
                    return True
            
            que.append(node.left)
            que.append(node.right)
        
        return False



    def isSameTree(self, p, q):
        if not p or not q:
            return False

        que = deque()
        que.append((p, q))

        while que:
            p, q = que.popleft()

            if not p and not q:
                continue

            if not p or not q or p.val != q.val:
                return False

            que.append((p.left, q.left))
            que.append((p.right, q.right))

        return True
