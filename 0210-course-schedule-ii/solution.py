class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res=[]
        adj=defaultdict(list)
        indegree={}
        for a,b in prerequisites:
            adj[b].append(a)
            indegree[a]=indegree.get(a,0)+1
        que=deque([i for i in range(numCourses) if i not in indegree])
        while que:
            node=que.pop()
            res.append(node)
            neigh=adj[node]
            for i in neigh:
                indegree[i]-=1
                if indegree[i]==0:
                    que.append(i)
        if len(res)==numCourses:
            return res
        else:
            return []
