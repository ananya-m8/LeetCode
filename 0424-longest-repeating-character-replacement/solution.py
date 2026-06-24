class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        f=defaultdict(int)
        res=0
        i=0
        n=len(s)
        for j in range(n):
            f[s[j]]+=1
            maxFreq=max(f.values())
            cur=j-i+1
            if cur-maxFreq>k:
                f[s[i]]-=1
                i+=1
            res=max(res,j-i+1)
        return res
