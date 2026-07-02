class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mind=0
        n=len(nums)
        for i in range(n):
            if i>mind:
                return False
            mind=max(mind,i+nums[i])
        return True
