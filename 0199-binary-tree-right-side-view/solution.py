# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res=[]
        def right(root,res,level):
            if not root:
                return -1
            if len(res)==level:
                res.append(root.val)
            right(root.right,res,level+1)
            right(root.left,res,level+1)
        right(root,res,0)
        return res
            
