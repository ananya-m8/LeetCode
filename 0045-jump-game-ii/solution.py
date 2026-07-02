class Solution:
    def jump(self, nums: List[int]) -> int:
        jump=0
        curend=0
        farth=0
        n=len(nums)
        for i in range(n-1):
            farth=max(farth,i+nums[i])
            if i==curend:
                jump+=1
                curend=farth
        return jump
