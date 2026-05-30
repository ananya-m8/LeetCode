class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        r=len(mat)
        s=0
        for i in range(r):
            s+=mat[i][i]+mat[i][r-i-1]
        if(r%2!=0):
            s-=mat[r//2][r//2]
        return s
