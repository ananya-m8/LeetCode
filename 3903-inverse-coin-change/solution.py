class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        n=len(numWays)
        ans=[]
        for i in range(0,n):
            if numWays[i]==1:
                ans.append(i+1)
                for j in range(n-1,i,-1):
                    numWays[j]=numWays[j]-numWays[j-i-1]
                numWays[i]=0
        if numWays!=[0]*n:
            return []
        else:
            return ans
