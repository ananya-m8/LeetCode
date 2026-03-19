class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l=1
        r=max(nums)
        while(l<=r):
            s=0
            mid=(l+r)//2
            for i in nums:
                s+=ceil(i/mid)
            if(s>threshold):
                l=mid+1
            else:
                r=mid-1
        return l
