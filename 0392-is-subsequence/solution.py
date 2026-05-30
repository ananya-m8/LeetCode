class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m=len(s)
        n=len(t)
        j=0
        for i in range(m):
            if(j<n and s[i]==t[j]):
                j+=1
            else:
                while(j<n and s[i]!=t[j]):
                    j+=1
                if(j==n):
                    return False
                j+=1
        return True
