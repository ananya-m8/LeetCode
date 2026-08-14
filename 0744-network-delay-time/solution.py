class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time=[float('inf')]*(n+1)
        time[k]=0
        adj=defaultdict(list)
        for src,dst,t in times:
            adj[src].append([dst,t])
        heap=[(0,k)]
        while heap:
            cur_t,node=heapq.heappop(heap)
            if cur_t>time[node]:
                continue
            for d,p in adj[node]:
                new_t=cur_t+p
                if new_t<time[d]:
                    time[d]=new_t
                    heapq.heappush(heap,(new_t,d))
        time.pop(0)
        if float('inf') in time:
            return -1
        else:
            return max(time)
