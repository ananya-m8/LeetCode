class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k%n
        l = nums[n-k:len(nums):1]
        l2 = nums[0:n-k]
        nums.clear()
        nums.extend(l+l2)
        
