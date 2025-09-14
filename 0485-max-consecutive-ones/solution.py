class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max = -1
        count=0
        for i in range(len(nums)):
            if(nums[i]!=1):
                if(max<count):
                    max = count
                count=0
            else:
                count+=1
        if(max<count):
            max = count
        return max
