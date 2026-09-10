class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)-1
        if grid[0][0]==1 or grid[n][n]==1:
            return -1
        queue=deque([[0,0,1]])
        grid[0][0]=1
        paths=([0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1])
        while queue:
            x,y,dist=queue.popleft()
            if x==y==n:
                return dist
            for i,j in paths:
                nx,ny=x+i,y+j
                if 0<=nx<=n and 0<=ny<=n and grid[nx][ny]==0:
                    queue.append([nx,ny,dist+1])
                    grid[nx][ny]=1
        return -1 
            
