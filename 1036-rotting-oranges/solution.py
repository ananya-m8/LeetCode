class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue=deque()
        fresh=0
        m=len(grid)
        n=len(grid[0])
        count=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        if fresh==0:
            return 0
        while queue and fresh>0:
            size=len(queue)
            for j in range(size):
                x,y=queue.popleft()
                if (x+1)<m and grid[x+1][y]==1:
                    fresh-=1
                    grid[x+1][y]=2
                    queue.append((x+1,y))
                if x-1>=0 and grid[x-1][y]==1:
                    fresh-=1
                    grid[x-1][y]=2
                    queue.append((x-1,y))
                if (y+1)<n and grid[x][y+1]==1:
                    fresh-=1
                    grid[x][y+1]=2
                    queue.append((x,y+1))
                if y-1>=0 and grid[x][y-1]==1:
                    fresh-=1
                    grid[x][y-1]=2
                    queue.append((x,y-1))
            count+=1
        if fresh==0:
            return count
        else:
            return -1
