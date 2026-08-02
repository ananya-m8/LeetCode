class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        colour=[-1]*n
        for i in range(n):
            if colour[i]!=-1:
                continue
            queue=deque([i])
            colour[i]=0
            while queue:
                node=queue.popleft()
                for j in graph[node]:
                    if colour[j]==-1:
                        colour[j]=1-colour[node]
                        queue.append(j)
                    elif colour[j]==colour[node]:
                        return False
        return True
