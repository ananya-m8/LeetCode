class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        l=[0,0]
        r=len(mat)
        for i in range(r):
            c=mat[i].count(1)
            if(c>l[1]):
                l=[i,c]
        return l
