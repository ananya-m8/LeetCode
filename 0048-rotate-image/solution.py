from math import floor
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(floor(n/2)):
            k=n-1-i
            for j in range(i,k):
                matrix[j][k],matrix[k][k-j+i],matrix[k-j+i][i],matrix[i][j]=matrix[i][j],matrix[j][k],matrix[k][k-j+i],matrix[k-j+i][i]
