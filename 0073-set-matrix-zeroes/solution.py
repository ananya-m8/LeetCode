class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        fnd=[]
        for i in range(m):
            ind=0
            chk=1
            while(0 in matrix[i][ind::]):
                chk=0
                fnd.append(matrix[i].index(0,ind))
                ind=fnd[-1]+1
            if(chk==0):
                matrix[i]=[0]*n
        print(matrix)
        fnd=set(fnd)
        print(fnd)
        for i in fnd:
            for j in range(m):
                print(j,i)
                matrix[j][i]=0

