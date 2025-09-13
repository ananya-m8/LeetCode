class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k=0
        c = nums.count(0)
        if(n==c):
            return
        for i in range(c):
            nums.remove(0)
        nums.extend([0]*c)
        
