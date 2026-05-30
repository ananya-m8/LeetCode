class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        s=sum(nums)
        l=[]
        s2=0
        for i in nums:
            while(i>0):
                s2+=i%10
                i//=10
        return abs(s-s2)
