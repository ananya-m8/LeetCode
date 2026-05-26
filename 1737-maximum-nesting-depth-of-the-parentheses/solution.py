class Solution:
    def maxDepth(self, s: str) -> int:
        count=0
        max_ct=0
        for i in s:
            if(i=='('):
                count+=1
            elif i==')':
                max_ct=max(max_ct,count)
                count-=1
        return max_ct
