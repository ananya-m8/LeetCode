class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        k=j=1
        while(j<len(nums)):
            if(nums[i]!=nums[j]):
                nums[i+1] = nums[j]
                k+=1
                i+=1
            j+=1
        nums = nums[0:i+1]
        return k

