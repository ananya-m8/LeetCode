class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum=nums[0]
        minSum=nums[0]
        currMin=nums[0]
        currMax=nums[0]
        total=nums[0]
        n=len(nums)
        for i in range(1,n):
            currMax=max(nums[i],currMax+nums[i])
            maxSum=max(currMax,maxSum)
            currMin=min(nums[i],currMin+nums[i])
            minSum=min(currMin,minSum)
            total+=nums[i]
        circle=total-minSum
        if circle==0:
            return maxSum
        return max(circle,maxSum)
