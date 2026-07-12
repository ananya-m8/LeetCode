# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l=[]
        def order(root,l):
            if not root:
                return
            l.append(root.val)
            order(root.left,l)
            order(root.right,l)
        order(root,l)
        n=len(l)
        for i in range(n):
            if k-l[i] in l[0:i]+l[i+1:]:
                return True
        return False
