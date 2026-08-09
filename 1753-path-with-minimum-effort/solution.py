import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r=len(heights)
        c=len(heights[0])
        efforts=[[float('inf')]*c for _ in range(r)]
        efforts[0][0]=0
        heap=[(0,0,0)]
        dir=[(1,0),(0,1),(-1,0),(0,-1)]
        while heap:
            eff,x,y=heapq.heappop(heap)
            if x==r-1 and y==c-1:
                return eff
            if eff>efforts[x][y]:
                continue
            for i,j in dir:
                nx=x+i
                ny=y+j
                if 0<=nx<r and 0<=ny<c:
                    diff=abs(heights[nx][ny]-heights[x][y])
                    new_eff=max(eff,diff)
                    if new_eff<efforts[nx][ny]:
                        efforts[nx][ny]=new_eff
                        heapq.heappush(heap,(new_eff,nx,ny))
        return 0

