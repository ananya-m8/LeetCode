class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m=len(isWater)
        n=len(isWater[0])
        queue=deque()
        height=[[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                height[i][j]=-1
                if isWater[i][j]==1:
                    height[i][j]=0
                    queue.append((i,j))
        dir=[(-1,0),(1,0),(0,1),(0,-1)]
        while(queue):
            r,c=queue.popleft()
            for i,j in dir:
                nr,nc=r+i,c+j
                if 0<=nr<m and 0<=nc<n and height[nr][nc]==-1:
                    height[nr][nc]=height[r][c]+1
                    queue.append((nr,nc))
        return height
            
