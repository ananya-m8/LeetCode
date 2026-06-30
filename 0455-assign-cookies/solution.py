class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        n=len(s)
        m=len(g)
        i,c=0,0
        for j in s:
            if i<m and g[i]<=j:
                c+=1
                i+=1
        return c
