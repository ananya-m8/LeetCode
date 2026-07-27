class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        r=len(mat)
        c=len(mat[0])
        res=[[0]*c for i in range(r)]
        que=deque()
        for i in range(r):
            for j in range(c):
                if mat[i][j]==1:
                    res[i][j]=-1
                else:
                    que.append((i,j))
        while que:
            x,y=que.popleft()
            if x-1>=0 and res[x-1][y]==-1:
                res[x-1][y]=res[x][y]+1
                que.append((x-1,y))
            if x+1<r and res[x+1][y]==-1:
                res[x+1][y]=res[x][y]+1
                que.append((x+1,y))
            if y-1>=0 and res[x][y-1]==-1:
                res[x][y-1]=res[x][y]+1
                que.append((x,y-1))
            if y+1<c and res[x][y+1]==-1:
                res[x][y+1]=res[x][y]+1
                que.append((x,y+1))
        return res
