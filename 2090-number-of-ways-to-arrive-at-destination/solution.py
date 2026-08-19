class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod=1000000007
        adj=[[] for _ in range(n)]
        for u,v,time in roads:
            adj[u].append((v,time))
            adj[v].append((u,time))
        dist=[float('inf')]*n
        ways=[0]*n
        dist[0]=0
        ways[0]=1
        priq=[(0,0)]
        while priq:
            d,u=heapq.heappop(priq)
            if d>dist[u]:
                continue
            for v,time in adj[u]:
                new_dist=d+time
                if new_dist<dist[v]:
                    dist[v]=new_dist
                    ways[v]=ways[u]
                    heapq.heappush(priq,(new_dist,v))
                elif new_dist==dist[v]:
                    ways[v]=(ways[v]+ways[u])%mod
        return ways[n-1]
