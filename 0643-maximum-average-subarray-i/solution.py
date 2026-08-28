class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        max_avg=sum(nums[0:k])
        s=max_avg
        for i in range(k,n):
            s=s-nums[i-k]+nums[i]
            max_avg=max(s,max_avg)
        return max_avg/k
