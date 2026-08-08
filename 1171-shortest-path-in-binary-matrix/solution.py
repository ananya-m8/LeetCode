class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1:
            return -1
        queue=deque([[0,0,1]])
        n=len(grid)-1
        paths=([0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1])
        while queue:
            x,y,dist=queue.popleft()
            if x==y==n:
                return dist
            if x-1>=0 and grid[x-1][y]==0:
                queue.append([x-1,y,dist+1])
                grid[x-1][y]=1
            if x+1<=n and grid[x+1][y]==0:
                queue.append([x+1,y,dist+1])
                grid[x+1][y]=1
            if y-1>=0 and grid[x][y-1]==0:
                queue.append([x,y-1,dist+1])
                grid[x][y-1]=1
            if y+1<=n and grid[x][y+1]==0:
                queue.append([x,y+1,dist+1])
                grid[x][y+1]=1
            if x-1>=0 and y-1>=0 and grid[x-1][y-1]==0:
                queue.append([x-1,y-1,dist+1])
                grid[x-1][y-1]=1
            if x+1<=n and y+1<=n and grid[x+1][y+1]==0:
                queue.append([x+1,y+1,dist+1])
                grid[x+1][y+1]=1
            if x+1<=n and y-1>=0 and grid[x+1][y-1]==0:
                queue.append([x+1,y-1,dist+1])
                grid[x+1][y-1]=1
            if x-1>=0 and y+1<=n and grid[x-1][y+1]==0:
                queue.append([x-1,y+1,dist+1])
                grid[x-1][y+1]=1
        return -1 
            
