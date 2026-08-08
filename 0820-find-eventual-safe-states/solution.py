class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        rev_g=[[] for i in range(n)]
        for i in range(n):
            for j in graph[i]:
                rev_g[j].append(i)
        indegree=[0]*n
        que=deque()
        for i in range(n):
            indegree[i]=len(graph[i])
            if indegree[i]==0:
                que.append(i)
        res=[]
        while que:
            node=que.pop()
            res.append(node)
            for i in rev_g[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    que.append(i)
        res.sort()
        return res
