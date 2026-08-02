class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r=len(grid)
        c=len(grid[0])
        def bfs(i,j,grid):
            if grid[i][j]=='1':
                grid[i][j]=0
                if i-1>=0 and grid[i-1][j]=='1':
                    bfs(i-1,j,grid)
                if i+1<r and grid[i+1][j]=='1':
                    bfs(i+1,j,grid)
                if j-1>=0 and grid[i][j-1]=='1':
                    bfs(i,j-1,grid)
                if j+1<c and grid[i][j+1]=='1':
                    bfs(i,j+1,grid)
        count=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]=='1':
                    count+=1
                    bfs(i,j,grid)
        return count
                    
