class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        sum1 = sum(nums)
        sum2 = 0
        set1 = set(nums)
        for i in set1:
            sum2+=i
        return 2*sum2-sum1
