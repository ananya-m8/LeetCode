class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m=len(mat)
        n=len(mat[0])
        low=0
        high=n-1
        while(low<=high):
            mid=(low+high)//2
            row=0
            for i in range(m):
                if(mat[i][mid]>mat[row][mid]):
                    row=i
            left=mat[row][mid-1] if(mid-1>=0) else -1
            right=mat[row][mid+1] if(mid+1<n) else -1
            tgt = mat[row][mid]
            if(tgt>left and tgt>right):
                return [row,mid]
            elif(tgt<left):
                high=mid-1
            else:
                low=mid+1
