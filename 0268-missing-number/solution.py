class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1 = sum(nums)
        sum2 = len(nums)*(len(nums)+1)/2
        return int(sum2-sum1)
        
