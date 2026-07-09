# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        if not root:
            return res
        que=deque([root])
        l=True
        while que:
            size=len(que)
            level=[0]*size
            for i in range(size):
                node=que.popleft()
                index=i if l else size-i-1
                level[index]=node.val
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            l=not l
            res.append(level)
        return res
