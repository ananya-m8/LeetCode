class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        neg=1
        pos=0
        mod=[0]*n
        for i in nums:
            if(i>=0):
                mod[pos] = i
                pos+=2
            else:
                mod[neg] = i
                neg+=2
        return mod
