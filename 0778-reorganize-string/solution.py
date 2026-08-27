class Solution:
    def reorganizeString(self, s: str) -> str:
        n=len(s)
        freq={}
        for i in s:
            freq[i]=freq.get(i,0)+1
        sortc=sorted(freq,key=lambda x:freq[x],reverse=True)
        if freq[sortc[0]]>(n+1)//2:
            return ''
        res=[None]*n
        i=0
        for j in sortc:
            for _ in range(freq[j]):
                if i>=n:
                    i=1
                res[i]=j
                i+=2
        return ''.join(res)
