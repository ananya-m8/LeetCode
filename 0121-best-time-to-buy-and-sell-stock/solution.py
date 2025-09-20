class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = 0
        profit=-1
        for  i in range(buy+1,n):
            if(prices[buy]<prices[i]):
                if(prices[i]-prices[buy]>profit):
                    profit = prices[i]-prices[buy]
            else:
                buy = i
                i = i+1
        if(buy==n-1 and profit==-1):
            return 0
        return profit
