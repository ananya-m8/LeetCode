class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        dp=[0]*(n+1)
        s_rev=s[::-1]
        for i in range(1,n+1):
            prev=0
            for j in range(1,n+1):
                temp=dp[j]
                if s[i-1]==s_rev[j-1]:
                    dp[j]=prev+1
                else:
                    dp[j]=max(dp[j],dp[j-1])
                prev=temp
        return dp[-1]
