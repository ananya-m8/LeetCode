class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]
        n=len(nums)
        for i in range(1,n):
            res.append(res[i-1]*nums[i-1])
        suff=1
        for i in range(n-1,-1,-1):
            res[i]*=suff
            suff*=nums[i]
        return res
