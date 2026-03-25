class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)
        n=len(nums)
        while(low<=high):
            mid=(low+high)//2
            temp=1
            s=0
            for i in range(n):
                if(s+nums[i]<=mid):
                    s+=nums[i]
                else:
                    temp+=1
                    s=nums[i]
            if(temp>k):
                low=mid+1
            else:
                high=mid-1
        return low
