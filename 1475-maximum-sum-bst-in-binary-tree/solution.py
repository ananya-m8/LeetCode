# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.maxSum=0
        def DFS(node):
            if not node:
                return (True,float('inf'),float('-inf'),0)
            left=DFS(node.left)
            right=DFS(node.right)
            if left[0] and right[0] and left[2]<node.val<right[1]:
                cur=node.val+left[3]+right[3]
                self.maxSum=max(self.maxSum,cur)
                return (True,min(left[1],node.val),max(right[2],node.val),cur)
            else:
                return (False,0,0,0)
        DFS(root)
        return self.maxSum
