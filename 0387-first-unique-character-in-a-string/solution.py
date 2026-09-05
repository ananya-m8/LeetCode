class Solution:
    def firstUniqChar(self, s: str) -> int:
        res=Counter(s)
        ind=float('inf')
        for i in res:
            if res[i]==1:
                ind=min(s.index(i),ind)
        if ind==float('inf'):
            return -1
        else:
            return ind
