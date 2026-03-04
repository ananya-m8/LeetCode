import math
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        spiral=[]
        iter = math.ceil(min(m,n)/2)
        top = 0
        bottom = m-1
        left = -1
        right = n-1
        for j in range(iter):
            left+=1
            for i in range(left,right+1):
                spiral.append(matrix[top][i])
            if(len(spiral)==m*n):
                return spiral
            top+=1
            for i in range(top,bottom+1):
                spiral.append(matrix[i][right])
            if(len(spiral)==m*n):
                return spiral
            right-=1
            for i in range(right,left-1,-1):
                spiral.append(matrix[bottom][i])
            if(len(spiral)==m*n):
                return spiral
            bottom-=1
            for i in range(bottom,top-1,-1):
                spiral.append(matrix[i][left])
        return spiral
