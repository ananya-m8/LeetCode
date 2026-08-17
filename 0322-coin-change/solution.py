class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res=[amount+1]*(amount+1)
        res[0]=0
        for i in range(amount+1):
            for j in coins:
                if j<=i:
                    res[i]=min(res[i],res[i-j]+1)
        return -1 if res[amount]==amount+1 else res[amount]
