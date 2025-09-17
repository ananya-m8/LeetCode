class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c1 = nums.count(2)
        c2 = nums.count(1)
        c3 = nums.count(0)
        nums.clear()
        nums.extend([0]*c3)
        nums.extend([1]*c2)
        nums.extend([2]*c1)
