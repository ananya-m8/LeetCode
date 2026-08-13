class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist=[float('inf')]*n
        dist[src]=0
        for i in range(k+1):
            temp=dist.copy()
            for s,d,pr in flights:
                if dist[s]!=float('inf'):
                    temp[d]=min(temp[d],dist[s]+pr)
            dist=temp
        return -1 if dist[dst]==float('inf') else dist[dst]

