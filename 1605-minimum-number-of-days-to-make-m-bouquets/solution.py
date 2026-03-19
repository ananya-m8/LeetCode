class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if(m*k>len(bloomDay)):
            return -1
        l=min(bloomDay)
        r=max(bloomDay)
        ans=-1
        while(l<=r):
            mid=(l+r)//2
            count=0
            boqt=0
            for bloom in bloomDay:
                if(bloom<=mid):
                    count+=1
                    if(count==k):
                        boqt+=1
                        count=0
                else:
                    count=0
            if(boqt>=m):
                ans=mid
                r=mid-1
            else:
                l=mid+1
        return l
