class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        q=deque()
        count=0
        for i in range(row):
            for j in range(col):
                if grid[i][j]==1:
                    count+=1
        for i in range(col):
            if grid[0][i]==1:
                q.append((0,i))
                grid[0][i]=0
            if grid[row-1][i]==1:
                q.append((row-1,i))
                grid[row-1][i]=0
        for i in range(row):
            if grid[i][0]==1:
                q.append((i,0))
                grid[i][0]=0
            if grid[i][col-1]==1:
                q.append((i,col-1))
                grid[i][col-1]=0
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r,c=q.popleft()
            count-=1
            for i,j in directions:
                nr,nc=r+i,c+j
                if 0<=nr<row and 0<=nc<col and grid[nr][nc]==1:
                    grid[nr][nc]=0
                    q.append((nr,nc))
        return count
