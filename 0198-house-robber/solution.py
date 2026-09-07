class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        prev1,prev2=0,0
        for i in range(n):
            cur=max(prev2,prev1+nums[i])
            prev1=prev2
            prev2=cur
        return cur
