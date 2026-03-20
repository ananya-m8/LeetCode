class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        while(l<r):
            mid = (l+r)//2
            load,d=0,1
            for i in weights:
                if(load+i>mid):
                    d+=1
                    load=i
                else:
                    load+=i
            if(d>days):
                l=mid+1
            else:
                r=mid
        return l
