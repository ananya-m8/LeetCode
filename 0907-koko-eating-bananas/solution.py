class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        ans=r
        while(l<=r):
            total=0
            mid=(l+r)//2
            for p in piles:
                total+=ceil(p/mid)
            if(total<=h):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return ans
