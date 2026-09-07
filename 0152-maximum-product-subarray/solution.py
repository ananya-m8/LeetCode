class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        prev_max=nums[0]
        prev_min=nums[0]
        ans=nums[0]
        for j in range(1,n):
            i=nums[j]
            if i<0:
                cur_max=max(prev_min*i,i)
                cur_min=min(prev_max*i,i)
            else:
                cur_max=max(prev_max*i,i)
                cur_min=min(prev_min*i,i)
            ans=max(ans,cur_max)
            prev_max,prev_min=cur_max,cur_min
        return ans
